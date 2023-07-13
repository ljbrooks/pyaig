import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent/'..'))
import math
from scr.TermMgr import *
from scr.util import *
import pdb
sym = lambda t: t.symbol
from natsort import natsorted
from scr.TermMgr import *    
#from isort import *

#POS ='positive'
#NEG = 'negative'
class Term:                     # base
    inf = None
    #nid = lambda(i):i.nid
    def __init__(self, **kwargs):
        self.nid=None
        #self.termx=TermList.zero
        self.__dict__.update(kwargs)
        self.uid  = TermMgr.UID
        self.ptr = None         # point to the uniquified one
        self.alter =[]
        self.has_m2_inv_children = False    # m2 has inverted children
        TermMgr.UID+=1
        TermMgr.tmgr.append(self) # this is where it can uniquified
        #not 
        pass
    def __repr__(self):
        return str(self)
    #return f'{self.__class__.__name__}: {str(self)}'
    def __or__(self, b):
        assert False
        return TermMgr.builder.__or__(self,b)
    def __and__(self,b):
        assert False
        return TermMgr.builder.__and__(self,b)
    def __add__(self,b):
        assert False
        return TermMgr.builder.__add__(self,b)
    def sigma(self, *termx):
        assert False
        return TermMgr.builder.__sigma__(*termx)
    def __neg__(self):
        # this is needed
        return TermMgr.builder.__neg__(self)
    def __invert__(self):
        return TermMgr.builder.__invert__(self)
    def __hash__(self):
        return hash(self.uid)
    def re_eval(self):
        return self 
    @property
    def car(self):
        return self.termx[0]
    
    @property
    def alter0(self):
        return None if len(self.alter) == 0 else self.alter[0]

    def sort_rank(self):
        return [ self.rank, self.OP, self.uid]
    
    def __le__(self, b):
        return self.sort_rank() <= b.sort_rank()
    def __lt__(self, b):
        return self.sort_rank() < b.sort_rank()
    #return self.uid < b.uid

    def __len__(self):
        return len(self.termx)
    def __getitem__(self, i):
        return self.termx[i]

    pass

class TermInf(Term):
    rank = math.inf
    pass

class TermGroup:
    pass

class TermList(Term):           # 1D
    OP = 'tl'
    rank = None
    sort = natsorted
    zero = None
    def __init__(self, *termx, **kwargs):
        Term.__init__(self,**kwargs)
        if len(termx) == 1 and isinstance(termx[0] , list):
            termx = termx[0]
            pass 
        else:
            termx = list(termx)
        assert isinstance(termx, list)
        assert not isinstance (termx, TermList)
        self.tx = termx
        #list.__init__(self, termx)
        #isort(self)
        assert not isinstance(termx, TermList)
        self.changed = True
        pass
    def appendd(self, v):
        self.changed = True
        self.tx.append(v)
        pass
    def removee(self, v):
        self.changed = True
        l = len(self.tx)
        self.tx.remove(v)
        assert l == len(self)+1
        return 
    def __getitem__(self, i):
        return self.tx[i]
    def __len__(self,): return len(self.tx)
    def __setitem__(self, i,v):
        self.changed = True
        self.tx[i] = v
        pass

    def __add__(self, x):
        r = []
        self.clear()

        assert isinstance(x, TermList)
        r = merge(self, x)
        return r
    def __str__(self):
        return str(self.tx)
    pass

class TermListUnordered(TermList):
    pass

TermList.zero = TermList()
#print(TermList.zero)
#assert False

Term.inf = TermInf()

class Atom(Term):
    rank = 1
    OP='a'
    def __init__(self, nid):
        Term.__init__(self, nid = nid)
        self.termx = []
        pass
    def __str__(self):
        return self.nid
    def __l1str__(self):
        return str(self)
    pass


class ConstOne(Atom):
    rank = 0
    def __init__(self):
        Atom.__init__(self, '1')
        pass
    pass

def const1(): 
    return atom('1')

class Expr(Term):
    rank = 2
    def __init__(self, *termx, tl = None, **kwargs):
        Term.__init__(self, **kwargs)
        self.termx = TermList.zero
        if not tl is None:
            termx = tl
        elif isinstance(termx, TermList):
            self.termx = termx
        if len(termx) == 1 and isinstance(termx[0] , list):
            termx = termx[0]
            pass

        self.termx = list(tuple(termx)) if not isinstance(termx, TermList) else termx
        pass
    def __str__(self):
        return (' %s ' % self.OP).join(map(str, self.termx)) #+ f'[{self.nid}]'
    def __l1str__(self):
        return (' %s ' % self.OP).join(map(nid, self.termx)) #+ f'[{self.nid}]'
    pass

class ExprUnary(Term):
    rank = 3
    def __init__(self, *termx, **kwargs):
        Term.__init__(self, **kwargs)
        self.termx = list(tuple(termx))
        pass
    def __str__(self):
        return f'{self.OP}{self.termx[0]}'
    def __l1str__(self):
        return f'{self.OP}{uid(self)}'
    pass
class ExprSigma(Expr):
    OP='+'
    def re_eval(self):
        return reduce(lambda a,b: a+b, self.termx[1:], self.termx[0])
    pass

class ExprXor(Expr):
    OP='^'
    def re_eval(self):
        return reduce(lambda a,b: a^b, self.termx[1:], self.termx[0])
    pass

class ExprAnd(Expr):
    OP='&'
    def re_eval(self):
        return reduce(lambda a,b: a&b, self.termx[1:], self.termx[0])
    pass

class ExprConsp(Expr):
    OP=':'
    def re_eval(self):
        return self
    pass


class ExprOr(Expr):
    OP='|'
    def re_eval(self):
        return reduce(lambda a,b: a|b, self.termx[1:], self.termx[0])
    pass
class ExprNeg(ExprUnary):
    OP='-'
    def re_eval(self):
        r =  - self.termx[0]
        r.nid = self.nid
        return r
    pass

class ExprInv(ExprUnary):
    OP='~'
    def re_eval(self):
        r =  ~ self.termx[0]
        r.nid = self.nid
        return r
    pass

class Func (Expr):
    rank = 4
    def __init__(self, *args,tl = None, **kwargs):
        Expr.__init__(self, *args, tl=tl,**kwargs)
        assert tl is None or  isinstance(tl, TermList)
        pass
    def __str__(self):
        return f'{self.F}(%s)' % (','.join(map(str,self.termx))) #+ f'[{self.nid}]'
    def __l1str__(self):
        return f'{self.F}(%s)' % (','.join(map(nid,self.termx))) #+ f'[{self.nid}]'

    pass

class FuncPrim(Func):
    rank = 5
    pass
class FuncS(FuncPrim):
    OP= F = 's'
    def re_eval(self):
        return TermMgr.builder.s(self.termx) #reduce(lambda a,b: a|b, self.termx[1:], self.termx[0])
    pass

class FuncD(FuncPrim):
    OP= F = 'd'
    def re_eval(self):
        return TermMgr.builder.d(self.termx) #reduce(lambda a,b: a|b, self.termx[1:], self.termx[0])
    pass

class FuncC(FuncPrim):

    OP = F = 'm'
    def __init__(self, *args,tl = None, **kwargs):
        Func.__init__(self, *args, tl=tl, **kwargs)
        self.is_m2 = False
        
        pass
    def re_eval(self):
        return TermMgr.builder.c(self.termx, is_m2 = self.is_m2) #reduce(lambda a,b: a|b, self.termx[1:], self.termx[0])
    pass



def FuncM2(*termx, tl=None, **kwargs):
    r = FuncC(*termx, tl=tl, **kwargs)
    r.is_m2 = True
    r.F = r.OP = 'm2'
    return r

class FuncM23(FuncPrim):
    OP = F = 'm2'
    def re_eval(self):
        return TermMgr.builder.m2(self.termx) #reduce(lambda a,b: a|b, self.termx[1:], self.termx[0])
    pass

# class FuncSigma(Func):
#     OP = F = '+/>'              # foldl + 
#     def re_eval(self):
#         return TermMgr.builder.sigma(self.termx) #reduce(lambda a,b: a|b, self.termx[1:], self.termx[0])
#     pass


class FuncD(Func):
    OP = F = 'd'
    def re_eval(self):
        return TermMgr.builder.d(self.termx) #reduce(lambda a,b: a|b, self.termx[1:], self.termx[0])
    pass

def atom(s, **kwargs): return Atom(s, **kwargs)

class scr:
    s = FuncS
    c = FuncC
    d = FuncD
    m2 = FuncM2
    pass

def rewrite(tx, rewriter):
    old_eval = TermMgr.builder
    TermMgr.builder = rewriter
    r = rewrite_r(tx)
    TermMgr.builder = old_eval
    return r

def rewrite_r(tx):
    #print()
    #print('enter', tx)
    if isinstance(tx, list):
        return list(map(rewrite_r, tx))
    if not len(tx.termx): return tx
    if isinstance(tx, FuncC) :
        #if tx.is_m2:             pdb.set_trace()
        pass
    ax = rewrite_r(tx.termx)
    #print('ax here', ax)
    #print('was', tx)
    u = tx.__class__(*tuple(ax), nid=tx.nid) # here missed the m2
    if isinstance(tx, FuncC) :
        u.is_m2 = tx.is_m2
    a = u.re_eval() # fmap(rewrite_r, tx.termx)
    if isinstance(tx, FuncC) :
        a.is_m2 = tx.is_m2
        pass
    #    a = tx.__class__(*tuple(a), tx.nid)
    #print('exit', a, '\n     <--', tx)
    #print()
    return a

def shortkey(t:Term):
    assert isinstance(t, Term) or isinstance(t, list)
    if isinstance(t,Atom): return str(t)
    else:
        if isinstance(t, TermList):
            return str(sorted(list(map(lambda i:i.uid, t)))) # 

        elif isinstance(t, list):
            return str(sorted(list(map(lambda i:i.uid, t)))) # 
            pass
        else:
            return f'{t.OP}(%s)' % (shortkey(t.termx))
        pass
    pass

skip_atom = lambda noAtom: lambda i: not noAtom or not isinstance(i, Atom)

def pretty_(noAtom):
    def fn(t):
        return pretty(t, noAtom= noAtom)
    return fn


Depth = 0
def pretty(t, depth = 0, noAtom=False):
    global Depth
    Depth+=1
    indent = f'  {Depth}  '
    if isinstance(t, TermList):
        Depth-=1
        return ('{%s}\n'%t.uid) + ',\n'.join(fmap(pretty_(noAtom), filter(skip_atom(noAtom), t)) )
    elif isinstance(t, list):
        Depth-=1
        return ',\n'.join(fmap(pretty_(noAtom), filter(skip_atom(noAtom),t)))
    if isinstance(t, Atom) :
        r = ('{%s}'%t.uid) + str(t) 
    elif isinstance(t, Func):
        rx  = [pretty(i, depth+1, noAtom) for i in filter(skip_atom(noAtom), t.termx)]
        r =f'{t.OP}.{t.uid} ( %s)' % (f'\n{indent}'.join(pretty_(noAtom)(t.termx).splitlines()))
        Depth-=1
        return r
    elif isinstance(t, ExprUnary):
        r = f'{t.OP}.{t.uid} %s' % (pretty_(noAtom)(t.car))
    else:
        print(t)
        assert False
        pass
    Depth-=1
    return r

def short(t, depth = 0):
    return pretty(t, depth, noAtom=True)
def l1str(a):
    return a.__l1str__()
        
if __name__ == '__main__':

    for i in 'abcdefghijklmnopqrstuvwxyz':
        set_var = '%s = "%s"' % (i,i)
        exec(set_var)
        pass
    S = scr.s
    C = scr.c
    D = src.d
    a0 = S(a,b)
    print(a0)
    pass
