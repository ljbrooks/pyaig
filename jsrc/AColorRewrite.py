'''
This is to rewirte the wide AND gates with color rewrites, and possibly in the future to rewrite XOR chain.
'''
import history, sys
from AGuessGate import *
import pyaig
from autil.lit_util import *
class AColorRewrite:
    def __init__(self, aiger):
        if isinstance(aiger, str ) : aiger = pyaig.aig_io.read_aiger(aiger)
        self.aiger = aiger
        self.ag = AGuessGate(aiger)
        self.acc = self.ag.acc
        self.topox = self.acc.topox
        self.marked = self.compute_marked()
        self.new_aiger = pyaig.AIG()
        self.v2new = {}
        pass
    def get_wand(self, i):
        if not self.ag.is_gate(i, AGate_AND): return None
        return self.ag.get_gate(i, AGate_AND)
    
    # only rewrite wide AND gates
    def compute_marked(self):
        marked = [False] * self.acc.N

        for i in reversed(self.topox):
            w = self.get_wand(i)
            finx = w if w else self.aiger.get_fanins(i)
            for j in finx: marked[var(j)] = True
            pass
        pass
    def new_lit(self, lit):
        r = make_lit(self.v2new(var(lit)) , sign(lit))
        return r
    def map_a_wide_and(i):
        wand = self.ag.get_gate(i, AGate_AND)
        fn = lambda i: (self.acc.colorMap[var(i)].cid, self.acc.level[var(i)])
        ix = sorted(wand, key=fn)
        pass
        
    def create_new(self):
        pi_name = lambda i: self.aiger.get_name_by_id if i in self.aiger._id_to_name  else None
        for i in self.topox:
            if self.aiger.is_pi(i):
                self.v2new[var(i)] = self.new_aiger.create_pi(pi_name(i))
            else:
                assert self.aiger.is_and(i)
                if self.ag.is_gate(i, AGate_AND):
                    # got a wide gate
                    self.map_a_wide_and(i)
                else:
                    l,r = self.aiger.get_fanins(i)
                    l = self.new_lit(l)
                    r = self.new_lit(r)
                    self.v2new[var(i)] = self.new_aiger.create_and( l, r)
                    pass
                pass
            pass
        for po_id, po_fanin, po_type in self.aiger.get_pos():
            s = self.new_aiger.create_po(self.new_lit(po_fanin), po_type)
            assert s==po_id
            pass
        pass
    pass

if __name__ == '__main__':

    from filex import *
    if len(sys.argv)>1: f = sys.argv[1]
    
    ac = AColorRewrite(f)
    pass
