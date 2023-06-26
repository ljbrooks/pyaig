from collections import *
import pdb
from functools import *
from autil.lit_util import *
class AGate(list):
    def __init__(self, inputx, outputx, covered_litx=[]):
        list.__init__(self, inputx)
        self.covered_litx = covered_litx
        self.outputx = outputx
        pass
    def identify(self, lit):  assert False

    pass
class AGate_OR(AGate):
    name = 'OR'
    shape = 'plain'
    pass
class AGate_AND(AGate):
    name = 'AND'
    shape = 'rectangle'
    pass
class AGate_XOR(AGate):
    shape = 'diamond'
    name = 'XOR'
    pass

class AGate_NXOR(AGate):
    shape = 'pentagon'
    name = 'NXOR'
    pass

class AGate_PP(AGate):          # partial-product
    shape = 'dot'
    name = 'PP'
    pass

class AGate_XOR_chain(AGate):
    shape = 'Mdiamond'
    name = 'xor_chain'

    @staticmethod
    def identify ( acc,  xor):
        assert isinstance(acc.gatex[var(xor)][0], AGate_XOR)
        lx = list( AGate_XOR_chain._identify_r(acc, pure(xor)))
        faninx = list(filter(lambda i: i[1] == 0, lx))
        internalx = list(filter(lambda i: i[1] == 1, lx))
        faninx , _  = zip(*faninx)
        internalx , _ =  zip(*internalx)
        if len(lx) > 3: 
            print("Found xor_chain:", f"{var(xor)} = %s" % (" XOR ".join(map(lstr,faninx))))
            pass
        return xor, faninx, internalx
    
    @staticmethod
    def _identify_r ( acc, xor):
        #        if var(xor) == 81: pdb.set_trace()
        if not acc.is_xor(xor) : 
            yield xor, 0        # a leaf
        else:
            for input in acc.get_xor(xor):
                for i in AGate_XOR_chain._identify_r(acc, input):
                    yield i
                    pass
                pass
            yield xor, 1        # not a leaf
            pass
        pass
    pass

#is_xor = lambda a: isinstance(a, AGate_XOR) or isinstance(a, AGate_XOR_chain)

class AGate_Majority3(AGate):          # majority function
    shape = 'box3d'
    name = 'maj3'
    @staticmethod
    def identify ( aiger, and3):
        assert isinstance(and3, AGate_AND)
        f = and3.outputx[0]     # f is the output
        ixx = list(map(lambda i: aiger.get_fanins(i), and3)) # get the trans fanins
        i2x = list(set(sum(ixx,[])))
        if len(i2x)!= 3 : return None                   # should be 3 different fanins
        c= Counter(sum(ixx,[]))
        if [i[1] for i in c.items()] != [2]*3 : return None # each appears twice
        b = map(lambda i: i[0] != i[1], ixx)                 # none should appeared under 1,
        if sum(b) != 3: return False
        return AGate_Majority3( list(map(inv,i2x)),
                                [f],
                                and3)
    pass



def Identify_chain(acc, i, gate_type):
    g = acc.gatex[var(i)][0]
    f = pure(g.outputx[0])
    assert var(f) == var(i)
    assert isinstance(acc.gatex[var(f)][0], gate_type)
    assert acc.gatex[var(f)][0] == g
    
    lx = list(_Identify_chain_r(acc, pure(f), gate_type))
    
    faninx = list(filter(lambda i: i[1] == 0, lx))
    internalx = list(filter(lambda i: i[1] == 1, lx))
    faninx , _  = zip(*faninx)
    internalx , _ =  zip(*internalx)
    if len(lx) > 3: 
        print(f"Found chain {gate_type.__name__}:", f"{var(f)} = %s" % (" $ ".join(map(lstr,faninx))))
        print(internalx)
        pass
    return g, faninx, internalx

    
def _Identify_chain_r(acc, g, gate_type):
    if not acc.is_gate(g, gate_type): 
        yield g, 0
        return 

    for input in acc.get_gate(g, gate_type):
        for j in _Identify_chain_r(acc, input, gate_type):
            yield j
            pass
        pass
    yield g, 1
    
    pass
        
