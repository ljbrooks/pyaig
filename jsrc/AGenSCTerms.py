import sys,pdb
sys.path.append('..')
import pyaig
from AGuessGate import *
from AigerCoiCluster import *
from autil.lit_util import *
from scr.Term import *
from functools import *

and_all = lambda i: reduce(lambda a,b : a and b, i, True)
class AGenSCTerms:
    # generate sc term from aiger after AGuessGate
    def __init__(self, aiger, rootx=None):
        if isinstance(aiger, str) : aiger = pyaig.aig_io.read_aiger(aiger)
        self.aiger , self.rootx = aiger, rootx
        self.ag = AGuessGate(self.aiger, self.rootx)
#        print(self.ag.HAx)
        
        self.acc = self.ag.acc
        self.topox = self.acc.topox
        self.ppx = dict()
        
        self.identify_p_terms()
        self.identify_g_terms()
        self.gen_terms()
        pass
    
    def gen_terms(self):
        #print(self.ag.FAx)
        for i in self.topox:
            if var(i) in self.ag.FAx:
                #pdb.set_trace()
                if not var(i) in self.ag.xor3x: continue
                g = self.ag.FAx[var(i)][0]
                assert len(g)
                c = g.outputx[0]
                s = g.outputx[1] 
                print(g, s,c)
                print(f'n{var(c)} = !c(%s)'% (','.join(map(str,g))))
                lit_sign = lambda l: '' if not sign(l) else '!'
                print(f'n{var(s)} = %ss(%s)'% (lit_sign(s),','.join(map(str,g))))
                pass
            elif var(i)  in self.ag.FAx:
                pass
            pass
        pass
    def get_id_name(self, i):
        if i in self.aiger._id_to_name:
            return self.aiger._id_to_name[i].decode('utf-8')
        return None

    def get_pp_x_y(self, i):
        a,b = i[0], i[1]
        assert self.aiger.is_pi(a)
        assert self.aiger.is_pi(b)
        x = int(self.get_id_name(a).split('[')[1][:-1])
        y = int(self.get_id_name(b).split('[')[1][:-1])
        if self.get_id_name(a).split('[') == 'IN2':
            x.y = y,x
            pass
        return x,y

    def identify_p_terms(self):
        for i,ix  in map(lambda i: (i, self.aiger.get_fanins(i)), self.topox):
            if len(ix) != 2: continue
            tx = [ self.aiger.is_pi(ix[0]) ,  self.aiger.is_pi(ix[1]) , 
                   not sign(ix[0]),  not sign(ix[1])]
            if not and_all(tx) : continue
            x,y = self.ppx[var(i)] = self.get_pp_x_y(ix)
            print(f'pp{var(i)} = pp_{x}_{y}')
            pass
        pass
    def identify_g_terms(self):
        pass
    pass

if __name__ == '__main__':
    
    import filex

    f = filex .f
    if len(sys.argv)>1:
        f = sys.argv[1]
    asc = AGenSCTerms(f)
