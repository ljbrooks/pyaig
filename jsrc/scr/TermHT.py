from isort import *
import pdb
from scr.util import *
from scr.Term import *
from scr.TermFoldr import *

class TermHT:
    @staticmethod
    def key(a):
        if isA(Atom)(a):
            return str(a)
        elif isA(TermList)(a):
            return str([i.uid for i in a])
        elif isinstance(a, list):
            return str([i.uid for i in a])
        else:
            assert isinstance(a.termx, TermList)
            return f'{a.OP}(%s)'% (a.termx.uid) #[i.uid for i in a.termx])
        assert False
        pass
    
    def __init__(self):
        self.tb = {}            # map key to term
        self.uidMap = {}        # map uid to term
        pass

    def __insert__(self, a):
        assert isinstance(a, Term)
        assert isinstance(a, TermList) or not isinstance(a, list)
        if self.key(a) in self.tb:
            return self.tb[self.key(a)]
        else:
            self.tb[self.key(a)] = a
            pass
        return a
    def add_termlist(self, tl):
        assert isinstance(tl, list)
        assert not isinstance(tl, TermList)
        i = hasattr(tl, 'termx') 
        isort(tl)
        k = self.key(tl)
        if k in self.tb:
            r =  self.tb[k]
        else:
            r = TermList(*tuple(tl))
            assert not hasattr(r, 'termx')
            r =  self.__insert__(r)
            pass
        assert isinstance(r, TermList)
        return r

    def new_op(self, op_type, lx):
        #pdb.set_trace()
        if not isinstance(lx, TermList):
            lx = self.add_termlist(lx)
            pass
        assert isinstance(lx, TermList)

        r = op_type(None,tl=lx)
        assert isinstance(r.termx , TermList)
        return self.update(r)
    
    def register(self,a):
        assert isinstance(a.termx, TermList)
        if len(a.termx):
            for i in range(len(a.termx)):
                a.termx[i] = self.tb[self.key(a[i])]
                pass
            assert isinstance(a.termx, TermList)
            isort(a.termx)      # insertion sort it
            assert isinstance(a.termx, TermList)
            assert not hasattr(a.termx, 'termx')
            a.termx = self.__insert__(a.termx)
            pass
        return self.__insert__(a)
    
    def update(self, a):
        assert isinstance(a, Atom) or isinstance(a.termx, TermList)
        if isinstance(a, Atom): return self.register(a)
        assert len(a.termx) >0
        if not isinstance(a.termx[0], Atom) and not isinstance(a.termx[0], FuncSigma):
            if not isinstance(a.termx, TermList):
                a.termx = self.add_termlist(a.termx)
                return self.register(a)
            pass
        atom_count = sum(map(lambda i: isinstance(i, Atom), a.termx))
        #if atom_count == 0: return self.register(a)
        #assert atom_count >0

        ax, bx  = a.termx[:atom_count], a.termx[atom_count:]
        if atom_count>0:

            f = FuncSigma(self.add_termlist(ax))
            f = self.register(f)
            bx = [f] + bx
            pass

        sigma_count = sum(map(lambda i: isinstance(i, FuncSigma), bx))
        if sigma_count > 1:
            ax, bx = bx[:sigma_count] , bx[sigma_count:]
            r = sum([i.termx.tx for i in ax], [])
            f = FuncSigma(self.add_termlist(r))
            bx = [f] + bx
            pass
        a.termx = self.add_termlist(bx)
        
        return self.register(a)

    pass
