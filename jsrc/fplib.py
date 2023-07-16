# constructive functional programming
from functools import *
import operator
def left_reduce( f, e):

    def fn(lx):
        return reduce(lambda a,b: f(a,b), lx, e)
    return fn


def left_reduce1( f):
    
    def fn(lx):
        assert len(lx) > 0
        return left_reduce(f, lx[0]) (lx[1:])
    return fn

def right_reduce(f,e):
    def fn(lx):
        r = e
        return reduce(lambda a,b: f(b,a) , reversed(list(lx)), e)
    return fn
        

def accumulate_l(f,e):#,  lx):
    
    def fn(lx):
        if not lx: return [e]
        
        # x = accumulate_l(f, e, lx[:-1])
        # y = x + [f(x[-1],lx[-1])]
        
        ff = lambda x, a: x + [ f(x[-1], a)]
        y = left_reduce(ff, [e])( lx)
        return y
    return fn

def accumulate_l1(f):
    def fn(lx):
        return accumulate_l(f, lx[0])( lx[1:])
    return fn


def accumulate_r(f, e):
    
    def fn(lx):
        #if not lx: return [e]
        ff = lambda a,b: [f (a,b[0])] + b 
        return right_reduce(ff, [e])(lx)
    return fn

def accumulate_r1(f):
    def fn(lx):
        return accumulate_r(f, lx[-1])(lx[:-1])
    return fn

def listify (x): return [x]


def fmap(f, lx): return list(map(f, lx))
def ffilter (p, lx): return list(filter(p, lx))


    
