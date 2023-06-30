'''
This is to rewirte the wide AND gates with color rewrites, and possibly in the future to rewrite XOR chain.
'''
import history, sys
sys.path.append('../')
import pdb
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
        self.v2new = [None] * self.acc.N
        r = self.create_new()
        
        pass
    def get_wand(self, i):
        if not self.ag.is_gate(i, AGate_AND): return None
        return self.ag.get_gate(i, AGate_AND)

    def get_xor(self, i):
        if not self.ag.is_gate(i, AGate_XOR): return None
        return self.ag.get_gate(i, AGate_XOR)
    
    # only rewrite wide AND gates
    def compute_marked(self):
        marked = [False] * self.acc.N 
        for i in self.aiger.get_po_fanins():
            marked[var(i)] = True
            pass
        for i in reversed(self.topox):
            xor = self.get_xor(i)
            w = self.get_wand(i) if xor is None else  xor # need to reconstruct the xor
            finx = w if w else self.aiger.get_fanins(i)
            for j in finx: marked[var(j)] = True
            pass
        return marked

    def map_lit(self, lit):
        r = self.v2new[var(lit)] ^sign(lit)
        return r
    def map_a_wide_and(self, i):
#        pdb.set_trace()
        wand = self.ag.get_gate(i, AGate_AND)

        fn = lambda i: (self.acc.colorMap[var(i)].cid,  self.acc.levelx[var(i)])
        ix = sorted(wand, key=fn) #, reverse=True)
        print('working on wand', var(i), ix)
        i0 = self.map_lit( ix[0])
        r = self.make_and_r(ix[0], i0, ix[1:])
        return r

    def get_cid(self, lit):
        return self.acc.colorMap[var(lit)].cid
    def create_and(self, l,r):
        if r is None: return l

        s =  self.new_aiger.create_and(l,r)

        print('create and', l, r, '->', s)
        return s
    def make_and_r(self, ex_i0, i0, ix):

        # car is the new lit
        if len(ix) == 0 : return i0
        i1 = ix[0]
        i0_cid = self.get_cid(ex_i0)
        i1_cid  = self.get_cid(i1)
        i1_mapped  = self.map_lit(i1)
        if i1_cid == i0_cid or len(ix)==1:
            print('and', ex_i0 , i1)
            n  = self.create_and(i0, i1_mapped)
            return self.make_and_r(ex_i0, n, ix[1:])
        else:
            n = self.make_and_r(i1, i1_mapped, ix[1:])
            return self.create_and(i0, n)
        pass

    def dup_gate(self, i):
        if not self.v2new[var(i)] is  None: return self.v2new[var(i)]
        l,r = self.aiger.get_fanins(i)
        l = self.map_lit(l)
        r = self.map_lit(r)
        self.v2new[var(i)] = self.create_and( l, r)
        return r
    def create_new(self):
        
        pi_name = lambda i: self.aiger.get_name_by_id(i) if i in self.aiger._id_to_name  else None
        for i in self.aiger.get_pis():
            self.v2new[var(i)] = self.new_aiger.create_pi(pi_name(i))
            pass
        for i in map(pure, filter(lambda v: self.marked[var(v)],self.topox)):
            #if var(i) == 37: pdb.set_trace()
            
            if self.aiger.is_pi(i):
                #self.v2new[var(i)] = self.new_aiger.create_pi(pi_name(i))
                continue
            else:
                assert self.aiger.is_and(i)
                if self.get_xor(i):
                    l,r = self.aiger.get_fanins(i)
                    self.dup_gate(l)
                    self.dup_gate(r)
                    self.dup_gate(i)
                    pass
                elif self.ag.is_gate(i, AGate_AND) :
                    # got a wide gate
                    r = self.map_a_wide_and(i)
                    self.v2new[var(i)] = r 
                else:
                    l,r = self.aiger.get_fanins(i)
                    l = self.map_lit(l)
                    r = self.map_lit(r)
                    self.v2new[var(i)] = self.create_and( l, r)
                    pass
                pass
            pass
        #pdb.set_trace()
        for (po_id, po_fanin, po_type), po_name  in zip(self.aiger.get_pos(), self.aiger.iter_po_names()):
            print('map po', po_fanin, 'to', self.map_lit(po_fanin))
            s = self.new_aiger.create_po(self.map_lit(po_fanin), 
                                         po_name[-1], 
                                         po_type)
            assert s==po_id
            pass
        pass
    pass

if __name__ == '__main__':

    from filex import *
    if len(sys.argv)>1: f = sys.argv[1]
    
    ac = AColorRewrite(f)
    
    pyaig.aig_io.write_aiger(ac.new_aiger, f'{f}.rock.aig')
    pass
