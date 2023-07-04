import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent/'..'))

from scr.VarBase import *
from scr.Frame import *

class FrameMgr:
    def __init__(self):
        self.cur = Frame()
        pass
    pass

class Var(VarBase):
    
    def __init__(self, name, val):
        assert isinstance(name, str) or name is None
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
        return defvar(val)
    def __and__(self,b):
        val = TermMgr.builder.__and__(self,b)
        return defvar(val)
    def __add__(self,b):
        assert False
        return defvar(TermMgr.builder.__add__(self,b))
    def sigma(self, *termx):
        assert False
        return defvar(TermMgr.builder.__sigma__(*termx))
    def __neg__(self):
        # this is needed
        return defvar(TermMgr.builder.__neg__(self))
    def __invert__(self):
        return defvar(TermMgr.builder.__invert__(self))
    def __hash__(self):
        return hash(self.uid)
    def re_eval(self):
        return self 

    def __le__(self, b):
        return self.uid <= b.uid

    def __call__(self, *args):
        # this is the apply
        self.termx = toList(*args)
        pass
    def __dot__(self, val):
        # this is com compose
        pass
    pass

class VarList(Var,list):
    @property
    def car(self):
        return self[0]
    @property
    def cedar(self):
        return self[1:]
    pass

def toList(*args):
    if len(args) == 1 and isinstance(args[0] ,list):
        return args[0]
    else : return lis(args)
    pass

def defvar(val=None, name=None):
    # here create a tmp var name
    return Var(name, val)

def use_space(K, gspace):
    gspace.update(K.exports())
    pass

