from fplib import *
import operator
def inits(lx):                  # include empty
    lxx = list(map(listify, lx))
    f = lambda a,b: a +b #+ [ a[-1] + b ]
    r = accumulate_l1(f)( lxx)
    return r

def tails(lx):                  # include empty
    lxx = list(map(listify, lx))
    #return accumulate_r(lambda a,b: a+b, [])( lxx)
    return accumulate_r1(lambda a,b: a+b)( lxx)
