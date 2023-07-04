from functools import *

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
        return sum(r) >= len(lx)//2 and sum(r) != 0
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


