from scr.Term import *
class TermBuilder:

    @staticmethod
    def __or__(a,b):
        return ExprOr(self,b)
    @staticmethod
    def __and__(self,b):
        return ExprAnd(self,b)
    @staticmethod
    def __add__(self,b):
        return ExprAdd(self,b)
    @staticmethod
    def __sigma__(self, *termx):
        return ExprSum(*termx)
    @staticmethod
    def __neg__(self):
        return ExprNeg(self)
    @staticmethod
    def __invert__(self):
        return ExprInv(self)
    @staticmethod
    def d(*termx):
        return FuncD(*termx)
    @staticmethod
    def s(*termx):
        return FuncS(*termx)
    @staticmethod
    def c(*termx):
        return FuncC(*termx)
    pass
