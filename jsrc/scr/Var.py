

class Var:
    def __init__(self, val=, name):
        self.name , self.val= name, val # 
        pass
    
    # got a new val
    def update(self, val):
        self.val = val
        pass

    def __repr__(self):
        #return f'{self.name}:{self.val}'
        return self.name
    #return f'{self.__class__.__name__}: {str(self)}'
    def __or__(self, b):

        val = TermMgr.builder.__or__(self.val, b.val)
        return var(val)
    def __and__(self,b):
        
        val = TermMgr.builder.__and__(self,b)
        return var(val)
    def __add__(self,b):
        assert False
        return var(TermMgr.builder.__add__(self,b))
    def sigma(self, *termx):
        assert False
        return var(TermMgr.builder.__sigma__(*termx))
    def __neg__(self):
        # this is needed
        return var(TermMgr.builder.__neg__(self))
    def __invert__(self):
        return var(TermMgr.builder.__invert__(self))
    def __hash__(self):
        return hash(self.uid)
    def re_eval(self):
        return self 
    @property
    def car(self):
        return self.termx[0]

    def __le__(self, b):
        return self.uid <= b.uid

    @staticmethod 
    def f(termx):
        r = FuncF(termx)
        return var(f)
    
    pass


def var(val=None, name=None):
    # here create a tmp var name
    return Var(name, val)

