
from AigerCoiCluster import *
from autil.lit_util  import *



class ARevEngAdder:

    def __init__(self, aiger, rootx = None, stopx = ()): # stopx is 
        self.aiger = aiger
        self.acc = AigerCoiCluster(self.aiger, rootx, stopx)
        self.ppx = [None] * self.acc.N # partial product
        pass


    def is_pp(self, i):
        l , r = self.aiger.get_fanins(i)
        if not sign(l) and sign(r): return True
        
        pass

    pass

if __name__ == '__main__':

    f = 'mock/d.aig'
    a = pyaig.aig_io.read_aiger(f)
    ar = ARevEngAdder(a)



