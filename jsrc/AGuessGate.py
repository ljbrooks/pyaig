import pyaig
from AigerCoiCluster import *
from AGate import *
def var(i) : return i//2
def lstr(i): return '%s%s'% ('+-'[sign(i)],var(i))
def sign(lit): return (lit &0x1) == 1
def ssign(lit): return '+-'[int(sign(lit))]
def inv(lit) : 
    if isinstance(lit, int):
        return lit ^ 0x1
    assert isinstance(lit, list)
    return list(map(inv, lit))
def pure(i): return i ^ (i&0x1)
class AGuessGate:

    def __init__(self, aiger, rootx=None):
        self.aiger , self.rootx = aiger, rootx
        if rootx is None: self.rootx = list(aiger.get_po_fanins())
        self.acc = AigerCoiCluster (aiger, rootx)
        self.gatex = [ [] for i  in self.acc.topox]
        for i in self.acc.topox:
            assert not sign(i)
            if self.acc.levelx[var(i)] >=2:
                self.identify_xor(i)
                pass
            self.extend_and(i)
            pass
        pass
    def print_gate(self,lit):
        l = self.aiger.get_and_left(lit)
        r = self.aiger.get_and_right(lit)
        ll = self.aiger.get_and_left(l)
        lr = self.aiger.get_and_right(l)
        rl = self.aiger.get_and_left(r)
        rr = self.aiger.get_and_right(r)
        
        r = '%s = %s( %s & %s ) & %s( %s & %s)' % (lstr(lit), 
                                                   ssign(l),
                                                   lstr(ll),
                                                   lstr(lr),
                                                   ssign(r),
                                                   lstr(rl),
                                                   lstr(rr))
        print(r)
        pass
    def extend_and(self, lit):
        kx = list(self._extend_and_r(lit))
        if lit == 96:
            print('yaya', kx)
            pass
        if len(kx)>2:
            print('found wide and%s @%s = AND %s'% (len(kx), var(lit), 
                                                    list(map(lambda i: (i[0], lstr(i[1])),kx))))
            pass
        pass
    def _extend_and_r(self, lit):
        if sign(lit): 
            yield (1, lit)
            return 
        if len(self.aiger.get_fanins(lit))!= 2: 
            yield (1, lit)
            return 
        #l,r = self.aiger.get_fanins(lit)
        for i in self.aiger.get_fanins(lit):
            for x, j in self._extend_and_r(i):
                yield (x, j)
                pass
            pass
        yield(0,lit)
        pass
    def identify_xor(self, lit):
        assert len(list(self.aiger.get_fanins(lit))) == 2
        l = self.aiger.get_and_left(lit)
        r = self.aiger.get_and_right(lit)
        l_fanin = sorted(list(self.aiger.get_fanins(l)))
        r_fanin = sorted(list(self.aiger.get_fanins(r)))
        if sign(l) and sign(r) and inv(l_fanin) == r_fanin:
            self.gatex.append(AGate_XOR([inv(r_fanin[0]), r_fanin[1]], lit, [l,r]))
                                        
            print('found ', var(lit), '%s = %s XOR %s' % ( var(lit), 
                                                           lstr(inv(r_fanin[0])), 
                                                           lstr(r_fanin[1])
                                                          ))
            self.print_gate(lit)
            
            return True
        else:
            return False
        pass
    pass
if __name__ == '__main__':
    f = 'mock/c.aig'
    f = 'mock/d.aig'
    a = pyaig.aig_io.read_aiger(f)
    ag = AGuessGate(a)
    outfname = str(Path(f).name[:-4] )+ '.dot'
    G = ag.acc.toDot(outfname)
