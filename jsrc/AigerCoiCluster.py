import pyaig
from  natsort import *
from dd.cudd import BDD

def var(i) : return i//2

class AigerCoiCluster:
    def __init__(self, aiger, rootx= None):
        self.aiger , self.rootx = aiger, rootx
        self.bddMgr = BDD()
        if rootx is None: self.rootx = list(aiger.get_po_fanins())
        self.nodex = list(aiger.topological_sort(self.rootx))
        self.N = max(map(lambda i: i//2, self.nodex))
        self.coix = [self.bddMgr.false for i in range(self.N+1)]
        self.init_pix()
        self.pox = [ self.coix[i//2] for i in self.aiger.get_po_fanins()]
        pass
    def init_pix(self):
        for i in self.nodex:
            var = i//2
            if self.aiger.is_pi(i):
                self.bddMgr.add_var(str(var))
                self.coix[var] = self.bddMgr.var(str(var))
                pass
            elif self.aiger.is_const0(i):
                self.coix[var] = self.bddMgr.false
            else:
                for j in self.aiger.get_fanins(i):
                    jvar = j//2
                    self.coix[var] = self.coix[var] | self.coix[jvar]
                    pass
                pass
            pass
        pass
    pass
if __name__ == '__main__':

   f = 'mock/c.aig'
#   f = 'mock/d.aig'
#   f = '/home/long/uu/pyaig/benchmarks/iscas-89/blif/c6288.aig'
   a = pyaig.aig_io.read_aiger(f)
   acc = AigerCoiCluster(a)
   bx = set(acc.coix)
   bx = [natsorted(i.support) for i in bx]
   bx = sorted(bx, key = lambda i: (len(i), i))
   list(map(print, bx))
   
   print('pox')
   pox = [natsorted(i.support) for i in acc.pox]
   list(map(print, pox))
   pass
