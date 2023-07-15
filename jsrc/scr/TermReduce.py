from scr.TermTopo import *
from collections import *
import pdb
from isort import isort
from scr.Term import *
from jtag3 import jtag

def jtag(*args): pass
class TermReduce:
    def __init__(self, term):
        self.term = term 
        self.topo = TermTopo([term])
        #print('\n'.join(map(str, self.topo.topoOrder())))
        self.x = list(self.dedup())
#        self.reduce(self.x[-1])
        pass
    def check(self,a):
        pass
    def wrap(self, lx):
        if isinstance(lx, list):
            return list(self.wrap(lx))
        return TermPtr(lx)
    
    def update(self, t: TermList):
        for i in range(len(t)):
            t[i] = self.d[shortkey(t[i])]
            pass
        isort(t)
        return t

    def dedup(self):

        # Atom is already unique, so let it go
        self.d = d = dict([(shortkey(i), i) for i in filter(lambda a: isinstance(a, Atom), self.topo.topoOrder())])
        
        for i in self.topo.topoOrder():
            if isinstance(i, Atom): continue
            #pdb.set_trace()
            self.update(i.termx)
            kx = shortkey(i.termx)
            #print('kx : ', kx)
            if kx not in d: 
                i.termx = TermList(i.termx)
                assert  i.termx.uid > 0
                d[kx] = i.termx
                pass
            else:
                i.termx = d[kx]
                pass
            k = shortkey(i)
            if k not in d :   d[k] = i
            else: 
                i = d[k] #assert False
                pass
            yield i
            pass
        return i
    def key_list(self, i):
        r = f'{i.OP}(%s)' % (list(map(lambda t: t.uid, i.termx)))
        return r
    def new(self, i, update=False):
        d = self.d

        i.termx = self.update(i.termx)
        kx = shortkey(i.termx)
        #print('kx : ', kx)
        if kx not in self.d: 
            i.termx = TermList(i.termx) if not isinstance(i.termx, TermList) else i.termx # i's term is updated
            assert  i.termx.uid > 0
            d[kx] = i.termx
            pass
        else:
            i.termx = d[kx]
            pass
        k = shortkey(i)
        if k not in d :   d[k] = i
        else : i = d[k]         # it is already there
        return i
    def reduce(self, a):
        #assert isinstance(a, FuncC)
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
        #print('common set:', set(cx.keys()) & set(csx.keys()))
        good = False
        for k  in cx.keys() & csx.keys(): # 
            good = True
            #pdb.set_trace()
            assert len(cx[k]) == 1
            assert len(csx[k]) == 1
            for c1, (c2, cs)  in zip( cx[k], csx[k]):
                
                jtag('reduce original): ', pretty(a))
                jtag('reduce m(x): ', pretty(c1))
                jtag('reduce m(s(x)+ m(y)): ', pretty(c2))
                c2x = [i for i in c2.termx] # this is s(x), m(y)
                c2x.remove(cs)              # 
                c2x.extend(cs.termx)        # 

                n = FuncC(c2x)
                n = self.new(n)
                n = self.reduce(n)
                #print(pretty(n))
                ax = [v for v in a.termx]
                ax.remove(c2)
                ax.remove(c1)
                ax.append(n) # this is correct
                a.termx = ax
                a = self.new(a)
                jtag('reduce result: ', pretty(a))
                pass
            break

        if good: return self.reduce(a)
        assert a.uid == u 
        return a
    def reduceAll(self, a):
        #if not isinstance (a, list): a = [a]
        assert isinstance(a, Func)
        topo = TermTopo([a])
        for i in topo.topoOrder():
            self.reduce(i)

            pass
        return a
    pass
        

    
