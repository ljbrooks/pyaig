from collections import *
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
                                f,
                                and3)
    pass



