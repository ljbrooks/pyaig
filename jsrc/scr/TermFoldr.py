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
        # x + fn(y)
        assert issubclass (ffn, Func)
        def f(a):
            #pdb.set_trace()
            assert isinstance(a, FuncPrim)
            if len(a.termx) != 2: return 
            if isA(FuncSigma)(a.termx[0]) and ffn.accept(a.termx[1]):
                x = a.termx[1].alter0
                if isinstance(x, ffn):
                    tx = [a.termx[0]] + [i for i in x.termx]
                else:
                    tx = [a.termx[0]] + [a.termx[1]]
                    pass
                #tx = ht.add_termlist(tx) #, ordered = False)
                tx = TermListUnordered(tx) # 
                r = ffn(tx)
                r = ht.update(r)# , ordered = False)
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

class FuncFoldrPlusM(FuncFoldr):
    # idetnify parallel prefix structure and reduce it
    F = OP = '+m</-'                 # rfold am
    
    accept  = lambda i: isA(FuncC)(i)

    @staticmethod
    def recognize(self):
        
        pass
    pass

class FuncFoldrMSPlus(FuncFoldr):
    F = OP = 'ms+<-/'                 # rfold m
    pass


class FuncReduceMMS(FuncFoldr):
    # f x:y:z = m ( m(y, sz), s( x, my) ) 
    # f x:ys:z = m ( f ys:z) , s (+m</- x:ys)
    @staticmethod
    def accept(a):
        '''
        # termList is ordered
        m (m,s)
        s (sigma, m)
        '''
        r =  isA(FuncC)(a) and len(a.termx) == 2 # and isA(FuncS(a.termx[-1]))
        if not r: return False
        #m, s = a.termx[:-1], a.termx[-1]
        m,s = a.termx
        if not isA(FuncC)(m) or not isA(FuncS)(s): return False
        if len(m.termx) != 2 or len(s.termx)!=2: return False
        zx, y1 = m.termx[:-1], m.termx[-1]
        x, y2 = s.termx
        if y1.termx != y2.termx: return False
        FuncReduceMMS.recognize(a)
        return True
    @staticmethod
    def recognize(a):
        m, s = a.termx[:-1], a.termx[-1]
        m, s = a.termx
        #if len(m) ==1: m = m[0]
        zx, y1 = m.termx[:-1], m.termx[-1]
        x, y2 = s.termx
        if hasattr(m,'mms'): 
            #X, YS, Z = m.mms
            #X, YS, Z = x, [y1]+YS, Z
            #assert y1.termx == m.mms[0]
            #assert z == m.mms[1]
            mms = [x] + m.mms

        else:
            #X, YS, Z  = x, [y1], z
            mms = [x,y1.termx[0],zx]
            pass
        a.mms = mms
        pass
    pass
