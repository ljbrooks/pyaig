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
        elif isinstance(a, FuncC):
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
        elif isinstance(a, FuncC):
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
        if len(termx) == 1 and isinstance(termx[0] , list):
            termx = termx[0]
            pass
        return FuncD(termx)

    def s(self, *termx, **kwargs):
        print('rewrite s', termx)
        if len(termx) == 1 and isinstance(termx[0] , list):
            termx = termx[0]
            pass
        else: 
            termx = list(termx)
        print('s', termx)
        
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
            pass

        return FuncS(*tuple(tx),**kwargs)

    def c(self, *termx , **kwargs):
        #pdb.set_trace()
        if len(termx) == 1 and isinstance(termx[0] , list):
            termx = termx[0]
            pass
        print('c', termx)

        if mostly(tsign)(termx):
            termx = fmap(self.__invert__, termx)
            return ExprInv(FuncC(*tuple(termx)))

        return FuncC(*tuple(termx))
    
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


def tinvert_inverted(tx, cnt=-1):
    print(tx,cnt)

    if cnt == -1:
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
