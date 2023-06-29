'''
This is to rewirte the wide AND gates with color rewrites, and possibly in the future to rewrite XOR chain.
'''
import history
from AGuessGate import *



class AColorRewrite:
    def __init__(self, aiger):
        self.aiger = aiger
        self.ag = AGuessGate(aiger)
        self.acc = self.ag.acc
        self.topox = self.acc.topox
        
        pass
    pass

if __name__ == '__main__':

    pass
