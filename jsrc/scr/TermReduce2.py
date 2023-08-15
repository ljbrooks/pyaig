from scr.TermTopo import *
from collections import *
import pdb
from isort import isort
from scr.Term import *
from jtag3 import jtag
from scr.TermHT import *

def jtag (*args):
    pass
class TermReduce2:
    def __init__(self, term):
        self.ht = TermHT()
        #self.term = term 
        #self.topo = TermTopo([term])
        #print('\n'.join(map(str, self.topo.topoOrder())))

        self.topo = list(self.dedup(term))
        self.root = self.topo[-1]
        self.topo = TermTopo([self.root]) # new topo
#        self.reduce(self.x[-1])
        pass
    
    def dedup(self, a):
        topo = TermTopo([a])
        for i in topo.topoOrder():
            if not isinstance(i.termx, TermList):
                i.termx = self.ht.add_termlist(i.termx)
                pass
            #self.ht.renew(i)
            yield self.ht.update(i) # here, I merge the atom list
            pass
        pass

    def reduce(self, a):
        #if isinstance(a, FuncC) and a.is_m2: return 
        
        # this is the rewrite 
        # 
        u = a.uid
        is_c = lambda i: isinstance(i, FuncC) 
        is_s = lambda i: isinstance(i, FuncS)
        cx = defaultdict(list)
        csx = defaultdict(list)
        for i in filter(is_c, a.termx):
            cx[i.termx.uid] .append(i) # the c-term
            for j in filter(is_s, i.termx):
                csx[j.termx.uid] .append((i,j)) # the c-term and the s-term
                pass
            pass
        if set(cx.keys()) & set(csx.keys()) :
            print('common set:', set(cx.keys()) & set(csx.keys()))
            pass
        good = False
        for k  in cx.keys() & csx.keys(): # 
            good = True
            #pdb.set_trace()
            assert len(cx[k]) == 1
            assert len(csx[k]) == 1
            for c1, (c2, cs)  in zip( cx[k], csx[k]):
                ax = [u for u in a.termx]
                assert isinstance(c1.termx, TermList)
                assert isinstance(c2.termx, TermList)
                #jtag('reduce original): ', pretty(a))
                #jtag('reduce m(x): ', pretty(c1))
                #jtag('reduce m(s(x)+ m(y)): ', pretty(c2))
                c2x = [i for i in c2.termx] # this is s(x), m(y)
                t = len(c2x)
                c2x.remove(cs)              # 
                assert t == len(c2x) + 1
                c2x.extend(cs.termx)        # 
                isort(c2x)
                #pdb.set_trace()
                #print (a.uid)
                #if a.uid == 844: pdb.set_trace()
                c2x = self.ht.add_termlist(c2x)
                
                #u = n = FuncC(None, tl=c2x)
                
                n =self.ht.new_op(FuncC, c2x) # can not be m2

                #n = self.ht.update(u)
                #print(pretty(n))
                # gosh a great achievement, performance greatly improved right here. 
                n = self.reduce(n) # this can possibly be further reduced
                t = len(a.termx)
                ax.remove(c2)
                assert len(ax) == t-1
                ax.remove(c1)
                assert not c1 in ax
                assert not c2 in ax
                ax.append(n) # this is correct
                isort(a.termx)
                assert t ==  len(ax) +1
                a.termx = self.ht.add_termlist(ax)
                a = self.ht.update(a)
                #jtag('reduce result: ', pretty(a))
                
                pass
            break

        if good: return self.reduce(a)
        assert a.uid == u 
        return a
    def reduceAll(self, a):
        #pdb.set_trace()
        assert isinstance(a, list)
        topo = TermTopo(a)
        for i in topo.topoOrder():
            #if i.uid == 133 : pdb.set_trace()
            self.reduce(i)
            pass
        return a
    pass
        

    
