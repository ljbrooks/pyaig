from collections import defaultdict
import math
WHITE='white'
GRAY='gray'
BLACK='black'
#from scr.Term import *
from scr.TermMgr import *
class Nil:
    def __init__(self):
        self.nid = 'nil'
        pass
    def __str__(self): return 'nil'
    def __repr__(self): return 'nil'
    pass

nil = Nil()

is_nil = lambda i: isinstance(i, Nil)
class TermTopo:
    def __init__(self, termx, rootx=None):
        self.termx = termx
        self.rootx = rootx if not rootx is None else termx
        self.fanout= defaultdict(list)
        self.dfs()
        
        pass
    def init(self):
        for i in TermMgr.tmgr:#self.termx: 
            i.color = WHITE
            i.d = math.inf
            i.f = math.inf 
            i.pi = nil
            pass
    def dfs(self):
        self.init()
        self.time = 1
        for i in reversed(self.rootx):
            if i.color == WHITE:
                i.color = GRAY
                self.dfs_r(i)
                pass
            pass
        pass
        pass
    def dfs_r(self, t):
        t.d , self.time = self.time, self.time+1
        for j in t.termx:
            if j.color == WHITE:
                j.color = GRAY
                j.pi = t
                assert not t is None
                self.dfs_r(j)
                pass
            pass
        t.color = BLACK
        t.f , self.time = self.time, self.time+1
        pass
    pass
