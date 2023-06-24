
from dd.cudd import BDD
def lprint(*args):
    print (*args)
    pass

class Aiger2Bdd:
    # compute the Aiger as a BDD at each node
    def __init__(self, aiger, bddMgr= None):
        self.aiger = aiger 
        self.bddMgr = BDD() if bddMgr is None  else bddMgr
        a = aiger
        N = self.N = a.n_ands() + a.n_pis() + a.n_pos()
        self. bddx  = [None ] * N
        self.bddx[0] = ~ self.bddMgr.false
        print(self.bddMgr.statistics())
        pass
    def lit2func(self, lit):
        u = self.bddx[lit//2]
        lprint('finding', lit//2)
        assert not u is None
        if lit & 0x1 :  u = ~u
        return u
    def compute_fanin_count(self, topoListOfNodes):
        self.fanin_cnt = [0] * self.N
        for i in topoListOfNodes:
            var = i//2
            for j in self.aiger.get_fanins(i):
                tmp = j//2
                self.fanin_cnt[tmp] += 1
                pass
            pass
        pass
    def set_func(self, var, f):
        self.bddx[var]  = f
        lprint('set ', var)
        assert not f is None
        pass
    def build_bdd(self, topoListOfNodes):
        # [int]
        self.compute_fanin_count(topoListOfNodes)
        for i in topoListOfNodes:
            varId = i//2
            lprint('computing', i)
            if self.aiger.is_pi(i):
                self.bddMgr.add_var(str(varId))
                u = self.bddMgr.var(str(varId))
                self.set_func(varId, u)
            elif self.aiger.is_and(i):
                l = self.lit2func(self.aiger.get_and_left(i))
                r = self.lit2func(self.aiger.get_and_right(i))
                self.set_func(varId, l & r)
                #continue
                for j in [ x//2 for x in self.aiger.get_fanins(i)]:
                    self.fanin_cnt[j] -=1
                    if self.fanin_cnt[j] == 0:
                        t = self.bddx[j] 
                        self.bddx[j] = None
                        del t
                        lprint('let go', j)
                        pass
                    pass
                pass
            elif self.aiger.is_const0(i):
                continue
            else:
                assert False
            pass
        pass
    pass


