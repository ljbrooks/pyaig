
class Term:                     # base
    
    pass

class Atom(Term):
    def __init__(self, symbol):
        self.symbol = symbol
        pass
    def __str__(self):
        return self.symbol
    pass

class ConstOne(Atom):
    def __str__(self):
        return '1'
    pass

class Expr(Term):
    def __init__(self, *termx):
        self.termx = termx
        pass
    def __str__(self):
        return (' %s ' % self.OP).join(map(str, self.termx))
    def __or__(self, a,b):
        return ExprOr(a,b)
    def __and__(self, a,b):
        return ExprAnd(a,b)
    def __add__(self,a,b):
        return ExprAdd(a,b)
    def sigma(self, *termx):
        return ExprSum(termx)
    def __neg__(self, a):
        return ExprNeg(a)
    def __inv__(self, a):
        return ExprInv(a)
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

class ExprNeg(Expr):
    OP='-'
    pass

class ExprInv(Expr):
    OP='~'
    pass

class ExprOr(Expr):
    OP='|'
    pass

class Func (Expr):
    def __str__(self):
        return f'{self.F}(%s)' % (','.join(self.termx))
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
