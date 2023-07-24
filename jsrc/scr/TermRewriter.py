from scr.Term import *
from scr.util import *
import pdb
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

        if isinstance(a,ExprNeg):
            return a.termx[0]
        elif isinstance(a, FuncC) and not a.is_m2:
            #~c(~x, ~y)
            if all(tsign)(a.car.termx) or mostly(tsign)(a.car.termx):
                return FuncC(fmap(self.__neg__, a.car.termx))
            pass
        elif isinstance(a, FuncS):
            if all(tsign)(a.car.termx) or mostly(tsign)(a.car.termx):
                return FuncS(neg(a.car.termx))
            pass
        return ExprNeg(a)

    def __invert__(self,a):
        if isinstance(a,ExprInv):
            return a.termx[0]
        elif isinstance(a, FuncC) and not a.is_m2:
            #~c(~x, ~y)
            if all(tsign)(a.car.termx) or mostly(tsign)(a.car.termx):
                return FuncC(fmap(self.__invert__, a.car.termx))
            pass
        elif isinstance(a, FuncS):
            if all(tsign)(a.car.termx) or mostly(tsign)(a.car.termx):
                return FuncS(fmap(self.__invert__, a.car.termx))
            pass
        return ExprInv(a)


    def d(self, *termx):
        assert False
        if len(termx) == 1 and isinstance(termx[0] , list):
            termx = termx[0]
            pass
        return FuncD(termx)

    def s(self, *termx, **kwargs):
        #print('rewrite s', termx)
        if len(termx) == 1 and isinstance(termx[0] , list):
            termx = termx[0]
            pass
        else: 
            termx = list(termx)
            #print('s', termx)
        
        # here is a while loop
        
        while True:
            sx,a = split_by(isA(FuncS))(termx)
            tx = termx
            if len(sx):
                tmp = [i.termx if isA(FuncS)(i) else [i] for i in termx]
                tx = sum(tmp, [])
                pass
            # if len(ss) : tx = ss + a
            # else : tx = termx
            #tx = termx
            # if mostly(tsign)(tx):
            #     return ExprInv(self.s(fmap(self.__invert__, tx)))
            inv_cnt =  sum(fmap(tsign, tx))
            if inv_cnt >1:
                tx = tinvert_inverted(tx, inv_cnt //2 * 2)
                termx = tx
                pass
            else:
                break
            pass

        return FuncS(*tuple(tx),**kwargs)

    def c(self, *termx ,is_m2 = None, **kwargs):
        #        print(is_m2)
        #assert is_m2 == True
        assert is_m2 != None
        #if is_m2:pdb.set_trace()
        if len(termx) == 1 and isinstance(termx[0] , list):
            termx = termx[0]
            pass
        #print('c', termx)

        if not is_m2 and mostly(tsign)(termx) :
            #assert False
            termx = fmap(self.__invert__, termx)
            return ExprInv(FuncC(*tuple(termx)))

        r =  FuncC(*tuple(termx))
        r.set_is_m2 (is_m2)
        return r

    def m2(self, *termx , **kwargs):
        assert False
        return FuncM2(*tuple(termx))

    
    def neg(self, *ax):
        if isinstance(ax, list):
            return fmap(self.neg, ax)
        else:
            return ~ax
        pass
    pass

def tsign(term):
    return isinstance(term, ExprInv)
def tneg(term):
    return isinstance(term, ExprNeg)


def invert_node(a):
    if isA(FuncC) and a.is_m2:
        return ExprInv(a)
    else:
        pass
    pass

def tinvert_inverted(tx, cnt=-1):
    #print(tx,cnt)
    #pdb.set_trace()
    if cnt == -1:
        # what does it mean? invert all
        for i in range(len(tx)):
            if tsign(tx[i]): tx[i] = tx[i].car 
            pass
        pass
    else:
        for i in range(len(tx)):
            if tsign(tx[i]) and cnt>0: 
                cnt -=1
                tx[i] = tx[i].car
                if cnt == 0:break
                pass
            pass
        pass
    return tx
