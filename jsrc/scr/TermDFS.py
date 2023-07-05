from scr.Term import *

class TermDFS:
    def __init__(self, a):
        self.m = {}
        
        self.root = a
        self.topo = []
        self.dfs(a)
        pass
    
    def dfs(self,a):
        assert not a.uid  in self.m
        self.m[a.uid] = a
        if isinstance(a.termx, TermList):
            if a.termx.uid in self.m:
                assert self.m[a.termx.uid] is a.termx
            else:
                self.m[a.termx.uid] = a.termx
                pass
            pass
        else:
            assert isinstance(a, Atom)
            pass
        for i in a:
            if not i.uid in self.m:
                self.dfs (i)
                pass
            else:
                assert i is self.m[i.uid]
            pass
        self.topo.append(a)
        pass
    pass
