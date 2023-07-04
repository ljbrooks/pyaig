from scr.TermTopo import *
from collections import *
import pdb
from scr.Term import *
class TermReduce:
    def __init__(self, term):
        self.term = term 
        self.topo = TermTopo([term])
        print('\n'.join(map(str, self.topo.topoOrder())))
        self.x = list(self.dedup())
#        self.reduce(self.x[-1])
        pass
    def dedup(self):
        key = lambda i: f'{i.OP}(%s)' % (list(map(lambda t: t.uid, i.termx)))
        key_list = lambda ix: str(list(map(lambda i: i.uid, ix)))

        # Atom is already unique, so let it go
        self.d = d = dict([(i.uid, i) for i in filter(lambda a: isinstance(a, Atom), self.topo.topoOrder())])
        
        for i in self.topo.topoOrder():
            if isinstance(i, Atom): continue
            #pdb.set_trace()
            
            i.termx = [self.d[j.uid] if isinstance(j, Atom) else self.d[key(j)] for j in i.termx]
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
            if k not in d :   d[k] = i
            else: 
                i = d[k] #assert False
                pass
            yield i
            pass
        return i
    def key_list(self, i):
        r = f'{i.OP}(%s)' % (list(map(lambda t: t.uid, i.termx)))
        return r
    def new(self, i):
        d = self.d
        key = lambda i: f'{i.OP}(%s)' % (list(map(lambda t: t.uid, i.termx)))
        key_list = lambda ix: str(list(map(lambda i: i.uid, ix)))
        #pdb.set_trace()
        i.termx = [self.d[j.uid] if isinstance(j, Atom) else self.d[key(j)] for j in i.termx]
        i.termx = list(sorted(i.termx, key=lambda x: x.uid))
        kx = key_list(i.termx)
        print('kx : ', kx)
        if kx not in self.d: 
            i.termx = TermList(i.termx)
            assert  i.termx.uid > 0
            d[kx] = i.termx
            pass
        else:
            i.termx = d[kx]
            pass
        k = key(i)
        if k not in d :   d[k] = i
        else : i = d[k]
        return i
    def reduce(self, a):
        is_c = lambda i: isinstance(i, FuncC)
        is_s = lambda i: isinstance(i, FuncS)
        cx = defaultdict(list)
        csx = defaultdict(list)
        for i in filter(is_c, a.termx):
            cx[i.termx.uid] .append(i) # the c-term
            for j in filter(is_s, i.termx):
                csx[j.termx.uid] .append((i,j)) # the c-term and the s-term
                pass
            pass
        print('common set:', set(cx.keys()) & set(csx.keys()))
        good = False
        for k  in cx.keys() & csx.keys(): # 
            good = True
            #pdb.set_trace()
            assert len(cx[k]) == 1
            assert len(csx[k]) == 1
            for c1, (c2, cs)  in zip( cx[k], csx[k]):
                c2x = [i for i in c2.termx]
                c2x.remove(cs)
                c2x.extend(cs.termx)

                n = FuncC(c2x)
                n = self.new(n)
                print(pretty(n))
                a.termx.remove(c2)
                a.termx.remove(c1)
                a.termx.append(n)
                a = self.new(a)
                pass
            break
            pass
        if good: return self.reduce(a)
        return a

    pass
        

    
