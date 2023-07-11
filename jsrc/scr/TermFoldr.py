

'''There are two kinds of such pattersn, we should recognize such
recursive patterns, it is called left-reducer.

## define f 
f [] = 0
f [a] = m a
f (a,b) = m(a + b)

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

class FuncFoldr(Term):
    # idetnify parallel prefix structure and reduce it
    def __init__(self, lx):
        list.__init__(self, lx)
        pass
    pass

class FuncSigma(FuncFoldr):
    OP = '+/'      # sigma of atoms
    # idetnify parallel prefix structure and reduce it
    pass

class FuncFoldrMPlus(FuncFoldr):
    # idetnify parallel prefix structure and reduce it
    OP = 'm+<-/'                 # rfold m
    pass

class FuncFoldrMSPlus(FuncFoldr):
    OP = 'ms+<-/'                 # rfold m
    pass

