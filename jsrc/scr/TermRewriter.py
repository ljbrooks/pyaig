

class TermRewriter:
    def __init__(self):
        pass
    def __or__(self, a,b):
        return ExprOr(a,b)
    
    def __and__(self,a,b):
        return ExprAnd(a,b)

    def __add__(self,a,b):
        return ExprAdd(a,b)

    def __sigma__(self, *termx):
        return ExprSum(*termx)

    def __neg__(self, a):
        return ExprNeg(a)

    def __invert__(self,a)
        return ExprInv(a)

    def d(self, *termx):
        return FuncD(*termx)

    def s(self, *termx):
        return FuncS(*termx)

    def c(self, *termx):
        return FuncC(*termx)
    pass

