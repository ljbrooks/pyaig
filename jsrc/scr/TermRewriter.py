from scr.Term import *

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
        # --a is a
        r = - a
        if isinstance(a,ExprNeg):
            return a.termx[0]
        elif isinstance(a, FuncC):
            #~c(~x, ~y)
            if all(tsign)(a.car.termx) or mostly(tsign)(a.car.termx):
                return FuncC(neg(a.car.termx))
            pass
        elif isinstance(a, FuncS):
            if all(tsign)(a.car.termx) or mostly(tsign)(a.car.termx):
                return FuncS(neg(a.car.termx))
            pass
        return r

    def __invert__(self,a):
        r = ~a
        if isinstance(a,ExprInv):
            return a.termx[0]
        elif isinstance(a, FuncC):
            #~c(~x, ~y)
            if all(tsign)(a.car.termx) or mostly(tsign)(a.car.termx):
                return FuncC(neg(a.car.termx))
            pass
        elif isinstance(a, FuncS):
            if all(tsign)(a.car.termx) or mostly(tsign)(a.car.termx):
                return FuncS(neg(a.car.termx))
            pass
        return r

    def d(self, termx):
        return FuncD(termx)

    def s(self, termx):
        # merge all the s
        # s(s(a)+b) = s(a,b)
        a,sx = split_by(isA(FuncS))(termx)
        
        s = sum(fmap(lambda i: i.termx, sx), [])
        if not s: return a+s
        return termx

    def c(self, termx):
        
        return FuncC(termx)
    
    def neg(self, ax):
        if isinstance(ax, list):
            return fmap(self.neg, ax)
        else:
            return ~ax
        pass
    pass

def tsign(term):
    return isinstance(term, ExprNeg) or isinstance(term, ExprInv)

def split_by(f):
    def fn(lx):
        a = ffilter(f, lx)
        b = ffilter(lambda i: not f(i), lx)
        return a,b
    return fn

def isA(Type):
    def fn(a):
        return isinstance(a,Type)
    return fn
def all(f):
    def fn(lx):
        r = reduce (lambda a,b: a and f(b), lx,True)
        pass
    return fn

def almost(f):
    def fn(lx):
        r = fmap(f, lx)
        return sum(r) >= len(lx)//4 *3

    return fn

def mostly(f):
    def fn(lx):
        r = fmap(f, lx)
        return sum(r) >= len(lx)//2
    return fn


def some(f):
    def fn(lx):
        r = reduce (lambda a,b: a or f(b), lx, False)
        return r
    return fn

def fmap(f, lx):
    return list(map(f, lx))

def ffilter(f, lx):
    return list(filter(f, lx))

