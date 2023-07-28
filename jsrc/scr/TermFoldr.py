import pdb
from jtag3 import jtag
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
                x = a.termx[1].alter0 # this recursive identify
                if isinstance(x, ffn):
                    tx = [a.termx[0]] + [i for i in x.termx]
                else:
                    tx = [a.termx[0]] + [a.termx[1]]
                    pass
                #tx = ht.add_termlist(tx) #, ordered = False)
                tx = TermListUnordered(tx) # 
                r = ffn(tx)
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
    # looking for f a b = a + m b
    
    @staticmethod
    def accept(i):
        r = isA(FuncC)(i) and len(i.termx) == 2 and min(fmap(expr_level, i.termx) ) ==1 
        a =  on_cnt(isA(FuncC))(i.termx) == 1 # one of it is m-node
        #a = on_cnt(isA(FuncC))(i.termx) == 1
        return r and a

    @staticmethod
    def recognize(node):
        
        pass
    pass

class FuncFoldrMSPlus(FuncFoldr):
    F = OP = 'ms+<-/'                 # rfold m
    pass


class FuncFoldrMMS(FuncFoldr):
    # f x:y:z = m ( m(y, sz), s( x, my) ) 
    # f x:ys:z = m ( f ys:z) , s (+m</- x:ys)
    F = OP = 'mms<-/'
    @staticmethod
    def accept(a):
        '''
        # termList is ordered
        m (m,s)
        s (sigma, m)
        '''
        r =  isA(FuncC)(a) and len(a.termx) == 2 
        if not r: return False

        m,s = a.termx

        if not isA(FuncC)(m) or not isA(FuncS)(s): return False
        if len(m.termx) < 2 or len(s.termx)!=2: return False
        zx, y1 = m.termx[:-1], m.termx[-1]
        x, y2 = s.termx
        if y1.termx != y2.termx: return False
        FuncReduceMMS.recognize(a)
        return True
    @staticmethod
    def recognize(a):
        assert len(a.termx) == 2
        m, s = a.termx
        #if len(m) ==1: m = m[0]
        zx, y1 = m.termx[:-1], m.termx[-1]
        x, y2 = s.termx
        if hasattr(m,'mms'): 
            mms = FuncFoldrMMS(TermListUnordered([x] + [i for i in m.mms]))
        else:
            mms = FuncFoldrMMS(TermListUnordered([x,y1.termx[0],TermList(zx)]))
            pass
        a.mms = mms
        pass
    pass
FuncReduceMMS = FuncFoldrMMS

class ReduceFoldr:
    def __init__(self, ht):
        self.ht = ht
        pass
    def is_plusm(self, a):
        r =  len(a.termx) == 2 and off_cnt(isA(FuncC))(asList(a.termx)) ==1 and min(fmap(expr_level, a.termx)) == 1 and on_cnt(isA(FuncC))(asList(a.termx))>=1
        r = r and on_cnt(isA(ExprInv))(asList(a.termx)) == 0
        return r 
    
    def reduce_FoldrPlusM(self, node):
        def collect(x):
            if  not self.is_plusm(x):
                print(type(x), x)
                assert isA(FuncC)(x)
                print(x)
                #assert len(x.termx) == 1
                yield x#.termx[0]
                return 

            assert len(x.termx) == 2
            a,b = x.termx[0], x.termx[1]

            if not isA(FuncC)(a): a,b = b,a
            assert not isA(TermList)(b)
            yield b             # b is not the m-term
            assert isA(FuncC)(a) # follow the m-term
            
            for i in collect(a): yield i
            assert not isA(TermList)(i)
            pass
        if isA(FuncFoldrPlusM)(node): return False, node

        if not self.is_plusm(node) : return False, node
        
        rx =  list(collect(node))
        #assert rx[-1] is None
        
        if len(rx) > 1:
            jtag('here', fmap(str, rx))
            print(type(node))
            #assert isA(FuncC)(node)
            node.termx = TermList( FuncFoldrPlusM(TermListUnordered(*tuple(rx))))
            return True, node
        return False, node
    def reduce_FoldrMMS(self, node):
        if hasattr(node, 'mms'): return True, node.mms
        return False, node
    
    def reduce(self, node):
        ok, node = self.reduce_FoldrPlusM(node)
        assert not isA(TermList)(node)
        if not ok:
            ok , node = self.reduce_FoldrMMS(node)
            pass
        node.termx = TermList(fmap(self.reduce, node.termx))

        return node

    def reduce_r(self, node):
        
        pass
