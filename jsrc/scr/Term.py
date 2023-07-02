from scr.TermMgr import *
from scr.util import *
import pdb
sym = lambda t: t.symbol

from scr.TermMgr import *    
class Term:                     # base

    def __init__(self, **kwargs):
        self.nid=None
        self.termx=[]
        self.__dict__.update(kwargs)
        self.uid  = TermMgr.UID
        TermMgr.UID+=1
        TermMgr.tmgr.append(self)
        pass
    def __repr__(self):
        return str(self)
    #return f'{self.__class__.__name__}: {str(self)}'
    def __or__(self, b):
        return TermMgr.builder.__or__(self,b)
    def __and__(self,b):
        return TermMgr.builder.__and__(self,b)
    def __add__(self,b):
        return TermMgr.builder.__add__(self,b)
    def sigma(self, *termx):
        return TermMgr.builder.__sigma__(*termx)
    def __neg__(self):
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
    pass


class Atom(Term):
    def __init__(self, nid):
        Term.__init__(self, nid = nid)
        pass
    def __str__(self):
        return self.nid

    pass

class ConstOne(Term):
    def __init__(self):
        Term.__init__(self)
        self.nid = '1'
        pass
    def __str__(self):
        return '1'
    pass

class Expr(Term):
    def __init__(self, *termx, **kwargs):
        Term.__init__(self, **kwargs)
        if len(termx) == 1 and isinstance(termx[0] , list):
            termx = termx[0]
            pass
        self.termx = list(tuple(termx))
        pass
    def __str__(self):
        return (' %s ' % self.OP).join(map(str, self.termx)) #+ f'[{self.nid}]'
    pass

class ExprUnary(Term):
    def __init__(self, *termx, **kwargs):
        Term.__init__(self, **kwargs)
        self.termx = list(tuple(termx))
        pass
    def __str__(self):
        return f'{self.OP}{self.termx[0]}'
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
    def __init__(self, *args, **kwargs):
        Expr.__init__(self,*args, **kwargs)
        pass
    def __str__(self):
        return f'{self.F}(%s)' % (','.join(map(str,self.termx))) #+ f'[{self.nid}]'
    pass

class FuncS(Func):
    F='s'
    def re_eval(self):
        return TermMgr.builder.s(*tuple(self.termx)) #reduce(lambda a,b: a|b, self.termx[1:], self.termx[0])
    pass

class FuncC(Func):
    F = 'c'
    def re_eval(self):
        return TermMgr.builder.c(*tuple(self.termx)) #reduce(lambda a,b: a|b, self.termx[1:], self.termx[0])
    pass

class FuncD(Func):
    F = 'd'
    def re_eval(self):
        return TermMgr.builder.d(*tuple(self.termx)) #reduce(lambda a,b: a|b, self.termx[1:], self.termx[0])
    pass

class scr:
    s = FuncS
    c = FuncC
    d = FuncD
    pass

def rewrite(tx, rewriter):
    old_eval = TermMgr.builder
    TermMgr.builder = rewriter
    r = rewrite_r(tx)
    TermMgr.builder = old_eval
    return r

def rewrite_r(tx):
    print()
    print('enter', tx)
    if isinstance(tx, list):
        return list(map(rewrite_r, tx))
    if not len(tx.termx): return tx
    if isinstance(tx, FuncC) :
        #        pdb.set_trace()
        pass
    ax = rewrite_r(tx.termx)
    print('ax here', ax)
    print('was', tx)
    u = tx.__class__(*tuple(ax), nid=tx.nid)
    a = u.re_eval() # fmap(rewrite_r, tx.termx)
    #    a = tx.__class__(*tuple(a), tx.nid)
    print('exit', a, '\n     <--', tx)
    print()
    return a


def pretty(t, depth = 0):
    indent = '   '
    if isinstance(t, list):
        return ',\n'.join(fmap(pretty, t))
    if isinstance(t, Atom) :
        r = str(t)
    elif isinstance(t, Func):
        rx  = [pretty(i, depth+1) for i in t.termx]
        r =f'{t.F}( %s)' % (f'\n{indent}'.join(pretty(t.termx).splitlines()))
        return r
    elif isinstance(t, ExprUnary):
        r = f'{t.OP}%s' % (pretty(t.car))
    else:
        print(t)
        assert False

    return r
        
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
