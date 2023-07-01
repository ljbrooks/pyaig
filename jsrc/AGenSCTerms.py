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
        self.lit2symbolx = [None] * (self.acc.N*2)
        self.pycode = self.init_pycode()        
        self.identify_p_terms()
        self.identify_g_terms()

        self.gen_terms()
        self.close_code()
        pass
    def code(self, s):
        self.pycode.append(s) if isinstance(s, str) else self.pycode.extend(s)
        pass
    def init_pycode(self):
        s = '''from scr.Term import *

'''
        return [s]
    def close_code(self, fname ='s.py'):
        open(fname,'w').write('\n'.join(self.pycode))
        print(self.__class__.__name__,'Gen', fname)
        pass
    
    def gen_terms(self):
        #print(self.ag.FAx)
        lit_sign = lambda l: '' if not sign(l) else '!'
        get_symbol = lambda i: self.lit2symbolx[i]
        for i in self.topox:
            if var(i) in self.ag.HAx:
                if not self.ag.is_xor(i): continue
                assert not sign(i)

                g = self.ag.HAx[var(i)][0]
                c = g.outputx[0]
                s = g.outputx[1] 
                assert not sign(c) and not sign(s)
                self.lit2symbolx[pure(c)] = f'hc{c}'
                self.lit2symbolx[pure(c)^0x1] = f'!hc{c}'                

                self.lit2symbolx[pure(s)] = f'hs{s}'
                self.lit2symbolx[pure(s)^0x1] = f'!hs{s}'                

                print(f'h{c} = c(%s)'% (','.join(map(get_symbol,g))))
                print(f'h{s} = %ss(%s)'% (lit_sign(s),','.join(map(get_symbol,g))))

                pass
            elif var(i) in self.ag.FAx:
                if not self.ag.is_xor(i): continue
                assert not sign(i)
                self.lit2symbolx[i] = f'f{i}'
                self.lit2symbolx[i^0x1] = f'f{i^0x1}'
                #pdb.set_trace()
                if not var(i) in self.ag.xor3x: continue
                g = self.ag.FAx[var(i)][0]
                assert len(g)
                c = g.outputx[0]
                s = g.outputx[1] 
                self.lit2symbolx[pure(c)] = f'fc{c}'
                self.lit2symbolx[pure(c)^0x1] = f'fc{inv(c)}'                

                self.lit2symbolx[pure(s)] = f'fs{s}'
                self.lit2symbolx[pure(s)^0x1] = f'fs{inv(s)}'                

                assert not sign(c) and not sign(s)
                print(g, s,c)
                #print(list(map(get_symbol, g)))
                for v in g:
                    print(get_symbol(v))
                    pass
                
                print(f'fc{c} = c(%s)'% (','.join(map(get_symbol,g))))
                print(f'fc{c^0x1} = c(%s)'% (','.join(map(get_symbol,map(inv,g)))))

                print(f'fs{s} = s(%s)'% (','.join(map(get_symbol,g))))
                print(f'fs{s^0x1} = s(%s)'% (','.join(map(get_symbol,inv_one(g)))))
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
            assert not  sign(i)
            if len(ix) != 2: continue
            tx = [ self.aiger.is_pi(ix[0]) ,  self.aiger.is_pi(ix[1]) , 
                   not sign(ix[0]),  not sign(ix[1])]
            if not and_all(tx) : continue
            x,y = self.get_pp_x_y(ix)
            k = f'n{i} -- pp{i} = Atom("pp_{x}_{y}")'
            self.lit2symbolx[i]  = f'pp{i}'
            self.lit2symbolx[inv(i)]  = f'!pp{i}'
            print(k)
            self.code(k)
            
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
        pass
    asc = AGenSCTerms(f)
