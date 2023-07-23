import sys, pdb

sys.path.append("..")
import pyaig
from AGuessGate import *
from AigerCoiCluster import *
from autil.lit_util import *
from scr.Term import *
from functools import *
from aiger_util import *

and_all = lambda i: reduce(lambda a, b: a and b, i, True)
or_all = lambda i: reduce(lambda a, b: a or b, i, False)


class AGenSCTerms:
    # generate sc term from aiger after AGuessGate
    def __init__(self, aiger, rootx=None):
        if isinstance(aiger, str):
            aiger = pyaig.aig_io.read_aiger(aiger)
        self.aiger, self.rootx = aiger, rootx
        self.ag = AGuessGate(self.aiger, self.rootx)
        #        print(self.ag.HAx)

        self.acc = self.ag.acc
        self.topox = self.acc.topox
        self.lit2symbolx = [None] * (self.acc.N * 2)
        self.pycode = self.init_pycode()
        self.identify_p_terms()
        self.identify_g_terms()

        self.gen_terms()
        self.gen_rootx()
        self.close_code()
        pass

    def gen_rootx(self):
        px = [self.lit2symbolx[i] for _, i, _ in self.aiger.get_pos()]
        r = """pox = [%s]""" % (",".join(px))
        self.code(r)
        pass

    def code(self, s):
        sx = s if isinstance(s, list) else [s]
        self.pycode.extend(sx)

        pass

    def init_pycode(self):
        s = """from scr.Term import *
from scr.TermTopo  import *
from scr.TermDot  import *

"""
        return [s]

    def close_code(self, fname="s.py"):
        open(fname, "w").write("\n".join(self.pycode) + "\n")
        print(self.__class__.__name__, "Gen", fname)
        pass

    def compute_marked(self):
        marked = [False] * self.acc.N
        for i in self.aiger.get_po_fanins():
            marked[var(i)] = True
        for i in reversed(self.topox):  # only for those marked
            if not marked[var(i)]:
                continue
            if not self.lit2symbolx[i] is None:
                continue
            if self.aiger.is_pi(i):
                assert not (sign(i))
                self.lit2symbolx[i] = f"i{i}"
                self.lit2symbolx[inv(i)] = f"i{inv(i)}"
                self.code(f'i{i} = Atom("i{var(i)}")   ## ' + pi_name(self.aiger)(i))
                self.code(f"i{inv(i)} = ~ i{i}    ## " + pi_name(self.aiger)(i))
                pass
            g = self.ag.get_adder_gate(i)
            if g is None:
                g = self.aiger.get_fanins(i)
            for j in g:
                marked[var(j)] = True

            pass
        return marked

    def gen_terms(self):
        # print(self.ag.FAx)
        lit_sign = lambda l: "" if not sign(l) else "-"
        get_symbol = lambda i: self.lit2symbolx[i]
        self.marked = self.compute_marked()
        for i in self.topox:  # only for those marked
            if not self.marked[var(i)]:
                continue
            g = self.ag.get_adder_gate(i)
            # if i==46: pdb.set_trace()
            code = []
            if isinstance(g, AGate_Majority3):
                c = i
                self.lit2symbolx[pure(c)] = f"hc{c}"
                self.lit2symbolx[pure(c) ^ 0x1] = f"~hc{c}"

                code = [
                    f'hc{c} = scr.c(%s, nid="hc{c}")' % (",".join(map(get_symbol, g))),
                    f'hc{inv(c)} = scr.c(%s, nid="hc{inv(c)}")'
                    % (",".join(map(get_symbol, inv(g)))),
                ]

                pass
            elif isinstance(g, AGate_XOR):
                s = i
                self.lit2symbolx[pure(s)] = f"xs{s}"
                self.lit2symbolx[pure(s) ^ 0x1] = f"~xs{s}"
                code = [
                    f'xs{s} = %sscr.s(%s, nid="xs{s}")'
                    % (lit_sign(s), ",".join(map(get_symbol, g))),
                    f'xs{inv(s)} = %sscr.s(%s, nid="xs{inv(s)}")'
                    % (lit_sign(s), ",".join(map(get_symbol, inv(g)))),
                ]
                self.code(code)
                pass
            elif isinstance(g, AGate_WAND):
                assert False
                pass
            else:
                if not self.lit2symbolx[i] is None:
                    continue
                g = self.aiger.get_fanins(i)
                c = pure(i)
                self.lit2symbolx[pure(c)] = f"xc{c}"
                self.lit2symbolx[pure(c) ^ 0x1] = f"xc{inv(c)}"
                code = [
                    f'xc{c} = scr.m2(%s, nid="m2{c}")' % (",".join(map(get_symbol, g))),
                    f'xc{inv(c)} = ~ scr.m2(%s, nid="m2{inv(c)}")'
                    % (",".join(map(get_symbol, g)))
                    # f'xc{inv(c)} =  scr.c(%s, nid="m2{inv(c)}")'% (','.join(map(get_symbol,inv(g))))
                ]
                pass
            self.code(code)
            pass
        pass

    def get_id_name(self, i):
        if i in self.aiger._id_to_name:
            return self.aiger._id_to_name[i].decode("utf-8")
        return None

    def get_pp_x_y(self, i):
        a, b = i[0], i[1]
        assert self.aiger.is_pi(a)
        assert self.aiger.is_pi(b)
        x = int(self.get_id_name(a).split("[")[1][:-1])
        y = int(self.get_id_name(b).split("[")[1][:-1])
        if self.get_id_name(a).split("[") == "IN2":
            x.y = y, x
            pass
        return x, y

    def identify_p_terms(self):
        for i, ix in map(lambda i: (i, self.aiger.get_fanins(i)), self.topox):
            assert not sign(i)
            if len(ix) != 2:
                continue
            tx = [
                self.aiger.is_pi(ix[0]),
                self.aiger.is_pi(ix[1]),
                not sign(ix[0]),
                not sign(ix[1]),
            ]
            if not and_all(tx):
                continue
            x, y = self.get_pp_x_y(ix)
            k = f'pp{i} = Atom("pp_{x}_{y}")   # n{i} --'
            self.lit2symbolx[i] = f"pp{i}"
            self.lit2symbolx[inv(i)] = f"~pp{i}"
            print(k)
            self.code(k)

            pass
        pass

    def identify_g_terms(self):
        pass

    pass


if __name__ == "__main__":

    import filex

    f = filex.f
    if len(sys.argv) > 1:
        f = sys.argv[1]
        pass
    asc = AGenSCTerms(f)
    from run import *

    print("INFO:", "import run.py PASSED")
