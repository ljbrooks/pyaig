import math, pdb
from scr.Term import *
from scr.util import *
from jtag3 import jtag
from scr.TermRewriter import *
from collections import Counter
from scr.TermSOP import *
from tabulate import *
# convert TermSOP to TermHorner and then to +m</- ripple adder format

class TermHorner(Func):
    F=OP='th'
    pass
class ReduceHorner(Func):

    # 
    def __init__(self, ht):
        self.ht = ht
        pass
    
    #  f (p,g) t = g + p * t
    #  f_e </- [ (p,q)] is the horner term, e is the init value
    def reduce(self, node):
        if isA(FuncSOP) (node): return self.reduce_horner_from_SOP(node)
        node.termx = fmap(self.reduce, node.termx)
        return node

    def reduce_horner_from_SOP(self, node):
        if not isA(FuncSOP)(node): 
            return node
        
        terms = sum([ asList(i.termx) for i in node.termx], [])
        cnt = Counter(terms)
        print(tabulate(cnt.items()))
        ak = list(self.factorize(node.termx)) # fmap(lambda i: asList, node.termx))# (node.termx))
        print(pretty(ak))
        r = TermHorner(*tuple(ak))
        return r
    def factorize(self, nx):
        assert  all(isA(FuncWideAnd))(nx)
        nx = fmap(lambda i: asList(i.termx), nx)
        r = sum(list(self.factorize_r(nx)), [])
        assert len(r) %2 == 0   # oddd length
        #assert r[-1] == []
        # do something here
        print('result', ustr(r))
        return r
    def factorize_r(self, nx):
        # nx is a list of 
        #pdb.set_trace()
        terms = sum(nx, [])
        print('terms', ustr(terms))
        #assert False
        cnt = Counter(terms)
        p, mcnt  = maxf(lambda i:i[1])(cnt.items())
        if mcnt == 1:  
            # here is the hack
            # here it is a list of [cin,p], [g]
            assert len(nx) == 2
            nx = sorted(nx, key=lambda i: len(i))
            assert len(nx[1]) == 2
            assert len(nx[0]) == 1
            yield [nx[0][0], nx[1][1]]
            yield [nx[1][0], []]
            #yield [pick_column(0)(cnt.items()), []]
            return 
            pass
        print(p)
        yes, no  = split_by(contains(p))(nx)
        assert len(no) == 1
        assert len(no[0]) == 1
        print('nx', nx)
        print('p', p)
        print('yes', yes)
        print('no', no)
        # f (p,g) x = g+ px
        # g is no
        # p is p
        # x is  +/ yes
        

        yield [p, no[0][0] ]
        
        for j in self.factorize_r(fmap(fremove(p), yes)):
            yield j
            pass
        
        pass
    
    pass



