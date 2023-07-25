import math, pdb
from scr.Term import *
from scr.util import *

from scr.TermRewriter import *
# This is to recognize horner's rule, convert the expanded form into horner's rule


# a + bc + bcd + bcde = a + b( c+ (de))
# NOR( abc, cde, fg, h) 

class TermHorner(Func):
    
    pass

class TermWideNOR(Func):
    
    # looking for a NOR(abc, def, ag, uv)
    
    # issue is where to stop to look for the horner sum
    
    @staticmethod
    def accept(a):
        return isA(FuncC)(a) and a.is_m2
    
    @staticmethod
    def recognize(a):
        assert isA(FuncC)(a) and a.is_m2
        root, mids, leaves =  collect_wide_nor(a)
        assert root == a
        #print('leaves', type(leaves))
        assert isinstance(leaves, list)
        u = fmap(lambda i : tinv(i), leaves)
        print(ustr(u))

        r = FuncWideOR(*tuple(u))
        r.root = root
        r.mids = mids
        a.wnor = tinv(r)
        # a.wor = 
        return r 
        
    pass



GRAY ='GRAY'
BLACK='BLACK'
WHITE='WHITE'
class TermVisit:
    time_ = 0
    g_visit_cnt  = 0 
    @staticmethod 
    def new_visit():     
        TermVisit.g_visit_cnt +=1 
        TermVisit.time_ = 0
        pass
    @staticmethod
    def is_visited(a):
        return a.visit_cnt == Term.g_visit_cnt
    @staticmethod
    def set_gray(a):
        a.visit_cnt = Term.g_visit_cnt
        a.color == GRAY
        a.pi = None
        a.d, a.f = math.inf, math.inf
        pass
    @staticmethod
    def init(a):
        #a.visit_cnt = Term.g_visit_cnt
        
        a.color == WHITE
        a.pi = None
        a.d, a.f = math.inf, math.inf
        pass

    @staticmethod
    def is_white(a):
        return not TermVisit.is_visited(a)
    @staticmethod
    def color(a):
        return WHITE if not TermVisit.is_visited(a) else a.color
    @staticmethod
    def inc_time():
        TermVisit.time_ +=1
        return TermVisit.time_ -1
    pass

always_false = lambda i: False
always_true = lambda *i: True            
def tdfs(a, nodeCondition = always_true, edgeCondition = always_true):
    TermVisit.new_visit()
    assert TermVisit.color (a) == WHITE
    TermVisit.init(a)
    for i in tdfs_r(a, nodeCondition, edgeCondition): yield i
    pass


def tdfs_r(a, nodeCondition, edgeCondition):
    print(ustr(a))
    #if a.uid == 232: pdb.set_trace()
    assert TermVisit.color(a) == WHITE
    a.d  = TermVisit.inc_time()
    TermVisit.set_gray(a)
    
    assert isinstance (a.termx , TermList)
    
    if nodeCondition(a): 
        print('termx:', ustr([i for i in a.termx]))
        for i in a.termx:
            if not edgeCondition(a, i): continue
            if TermVisit.color(i) == WHITE:
                TermVisit.init(i)
                for j in tdfs_r(i, nodeCondition, edgeCondition): yield j
                pass
            pass
        pass
    yield a
    a.f  = TermVisit.inc_time()
    pass

def collect_wide_nor(a):
    # this thing is an invertor
    nodeCondition = lambda i: isA(FuncC)(i) and i.is_m2
    if not nodeCondition(a): return [a], [],[]
    edgeCondition = always_true #lambda u,v: isA(FuncC)(u) and u.is_m2 and not tsign(u)

    nx = list(tree_dfs(a, nodeCondition, edgeCondition))
    #if a.uid == 232: pdb.set_trace()
    rr =  ( nx[-1],            # root
             ffilter(nodeCondition, nx[:-1]), # middle 
             ffilter(lambda i: not nodeCondition(i), nx[:-1]))# stopCondition(nx[:-1])))     # leaves
    print(len(nx))
    assert len(rr[1] + rr[2]) == len(nx) -1
    return rr

inv_f = lambda fn: lambda *i: not fn(*i)

def collect_wide_and(a):        # a is inverted m2
    # this thing is an invertor
    nodeCondition = lambda i: isA(FuncC)(i) and i.is_m2
    edgeCondition = lambda u,v : True

    nx = list(tree_dfs(a, nodeCondition, edgeCondition))
    
    root, mids, leaves = ( nx[-1],            # root
                           ffilter(nodeCondition, nx[:-1]), # middle 
                           ffilter(inv_f(nodeCondition), nx[:-1]))
    if len(nx)==1: leaves = nx
    r = FuncWideAnd(*tuple(leaves))
    r.root , r.mids = root, mids
    a.wand = r
    return r
# just traverse it
def tree_dfs(a, nodeCondition, edgeCondition):
    if nodeCondition(a):
        for i in a.termx:
            for j in tree_dfs(i, nodeCondition, edgeCondition): yield j
            pass
        pass
    yield a
    pass

def expand_wide_or(top):
    # top is wor(x,y,z,w) and each term is a wide_and of terms, any of
    # leaves of the wide_and is an OR gate, it will then be expanded
    # into the top level term
    if tsign(top): top = top.car

    for i in top.termx:
        if hasattr(i, 'wand'):
            #assert False
            # i is a wand term
            for j in i.termx:
                if isA(ExprInv)(j):
                    #if hasattr(j, 'wnor'):
                    # we got a wor term
                    #assert False
                    print('i',ustr(i), i)
                    print('j', j)
                    print('j.car', j.car)
                    print('j.uid', ustr(j.car), ustr(j.car.termx.as_list))
                    
                    print(j.car.wnor)
                    assert False
                    pass
                pass
            pass
        pass
    
    pass
