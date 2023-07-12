import pdb

'''There are two kinds of such pattersn, we should recognize such
recursive patterns, it is called left-reducer.

## define f 
mm [] = 0
mm [a] =  a
mm (a,b) = m(a + b)

lfold(f) [a,b,c] = m(a+m(b+m(c))) 

lfold(m+)


## define g
g []= 0
g [a] = m a 
g (a,b) = m( s(a) + b)

lfold(g) [a,b,c]  = m(s(a) + m(s(b) + m c) )
lfold(ms+)

## 



## define m

m [] = 0
m x = floor( sum(x) )
m a = m [a]

## define s

s a = a % 2
s [a] = foldr ^ s*[a]

foldr s [a] = 

Theorem: 

lfold m+ x++[a] = (lfold m+  x) + (lfold ms+ a)

lfold ms+ a = (lfold m+ x++[a]) - (lfold m+  x) 

'''
import sys
sys.path.append('.')
from scr.Term import *

class FuncFoldr(Func):
    rank = 7
    # idetnify parallel prefix structure and reduce it
    def __init__(self, lx):
        assert isinstance(lx, TermList)
        Func.__init__(self, None, tl=lx)
            #list.__init__(self,  lx)
        pass
    @staticmethod 
    def recognize(ffn, ht):         # ffn : fold_fn
        assert issubclass (ffn, Func)
        # x + fn(y)
        def f(a):
            #pdb.set_trace()
            assert isinstance(a, FuncPrim)
            if len(a.termx) != 2: return 
            if isA(FuncSigma)(a.termx[0]) and isA(ffn.base_fn)(a.termx[1]):
                x = a.termx[1].alter0
                if isinstance(x, ffn):
                    tx = [a.termx[0]] + [i for i in x.termx]
                else:
                    tx = [a.termx[0]] + [a.termx[1]]
                    pass
                tx = ht.add_termlist(tx, ordered = False)
                r = ffn(tx)
                r = ht.update(r, ordered = False)
                a.alter.append(r)
                return r
            pass
        return f
    pass

class FuncSigma(FuncFoldr):
    rank = 3.5
    F = OP = '+/'      # sigma of atoms
    # idetnify parallel prefix structure and reduce it
    
    pass

class FuncFoldrMPlus(FuncFoldr):
    # idetnify parallel prefix structure and reduce it
    F = OP = 'm+<-/'                 # rfold m
    
    base_fn = FuncC

    @staticmethod
    def recognize(self):
        
        pass
    pass

class FuncFoldrMSPlus(FuncFoldr):
    F = OP = 'ms+<-/'                 # rfold m
    pass

