from scr.Term import *

from scr.util import *
class TermRule:
    def __init__(self):
        pass

    def match(self, term):
        assert False
        pass
    
    def reduce(self, term):
        assert False
        pass

    pass




class TermRule_Lemm2(TermRule):
    def __init__(self, *args):
        TermRule.__init__(*args)
        pass
    def match(self, term):
        # c(x + y) = d (x + y - s(x) - s(y))
        # c(\sigma x) = d( \sigma(x) - \sigma(s(x))
        
        pass
    def reduce(self, term):
        
        pass
    pass

class TermRule_dont_touch(TermRule):
    def __init__(self):
        pass
    def match(self, term):
        r = list(filter(isA(FuncS), term))
        pass
    pass
    
