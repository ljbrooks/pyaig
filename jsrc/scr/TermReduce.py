from scr.TermTopo import *
import pdb
from scr.Term import *
class TermReduce:
    def __init__(self, term):
        self.term = term 
        self.topo = TermTopo([term])
        print('\n'.join(map(str, self.topo.topoOrder())))
        self.x = list(self.dedup())
        pass
    def dedup(self):
        key = lambda i: f'{i.OP}(%s)' % (map(lambda t: t.uid, i.termx))
        key_list = lambda ix: str(list(map(lambda i: i.uid, ix)))

        # Atom is already unique, so let it go
        d = dict([(i.uid, i) for i in filter(lambda a: isinstance(a, Atom), self.topo.topoOrder())])
        
        for i in self.topo.topoOrder():
            if isinstance(i, Atom): continue
            #pdb.set_trace()
            i.termx = list(sorted(i.termx, key=lambda x: x.uid))
            kx = key_list(i.termx)
            print('kx : ', kx)
            if kx not in d: 
                i.termx = TermList(i.termx)
                assert  i.termx.uid > 0
                d[kx] = i.termx
                pass
            else:
                i.termx = d[kx]
                pass
            k = key(i)
            if k not in d[kx] :   d[k] = i
            yield i
            pass
        return i
    pass
        

    
