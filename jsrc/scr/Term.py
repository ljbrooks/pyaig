from scr.TermMgr import *

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
        return f'{self.__class__.__name__}: {str(self)}'
    def __or__(self, b):
        return ExprOr(self,b)
    def __and__(self,b):
        return ExprAnd(self,b)
    def __add__(self,b):
        return ExprAdd(self,b)
    def sigma(self, *termx):
        return ExprSum(termx)
    def __neg__(self):
        return ExprNeg(self)
    def __invert__(self):
        return ExprInv(self)
    def __hash__(self):
        return hash(self.uid)
    
    pass

def count(t):
    assert isinstance(t, Term)
    return 1 + sum(map(count, t.termx))

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
        self.termx = termx
        pass
    def __str__(self):
        return (' %s ' % self.OP).join(map(str, self.termx))
    pass
class ExprUnary(Term):
    def __init__(self, *termx, **kwargs):
        Term.__init__(self, **kwargs)
        self.termx = termx
        pass
    def __str__(self):
        return f'{self.OP}{self.termx[0]}'
    pass
class ExprSigma(Expr):
    OP='+'
    pass

class ExprXor(Expr):
    OP='^'
    pass

class ExprAnd(Expr):
    OP='&'
    pass

class ExprNeg(ExprUnary):
    OP='-'
    pass

class ExprInv(ExprUnary):
    OP='~'
    pass

class ExprOr(Expr):
    OP='|'
    pass

class Func (Expr):
    def __init__(self, *args, **kwargs):
        Expr.__init__(self,*args, **kwargs)
        pass
    def __str__(self):
        return f'{self.F}(%s)' % (','.join(map(str,self.termx)))
    pass

class FuncS(Func):
    F='s'
    pass

class FuncC(Func):
    F = 'c'
    pass

class FuncD(Func):
    F = 'd'
    pass

class scr:
    s = FuncS
    c = FuncC
    d = FuncD
    pass

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
