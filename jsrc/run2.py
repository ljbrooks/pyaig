from scr.TermTopo import *
import pdb
from scr.TermDot import *
from scr.TermMgr import *
from scr.TermBuilder import *
from scr.TermRewriter import *
from scr.TermReduce2 import *
from scr.TermDFS import *
import math
from tabulate import *
from scr.util import *
TermMgr.builder = TermBuilder
from s import *

print("INFO: pox = ", [i.nid for i in pox])

tm = TermMgr.tmgr

tx = list(filter(lambda i: i.nid, tm))


topo = TermTopo(pox)
tx = list(filter(lambda i: i.d != math.inf, tm))


def topoOrder(with_t=True):
    for t in sorted(tx, key=lambda i: i.f):
        print(t.color, t.d, t.f, t.nid, t.pi.nid, t.uid, "" if not with_t else t)
        pass
    pass


#print(tabulate([[i.nid, str(i)] for i in topo.topoOrder()]))


a = TermRewriter()

ux = pox
for u in ux:
#    print
    x= rewrite(u,a)
    #   print('before --')
    #print(pretty(u))
    #print('after-----')
    #print(pretty(x))
    #print()
#print(str(u))

rx = [rewrite(i,a) for i in pox]
'''
for i in pox:
    pdb.set_trace()
    u = rewrite(i,a)
    print(u)
'''



for i in rx:
    lx = [ len(TermTopo(i).topoOrder())]
    tr = TermReduce2(i)
    r = tr.root
    lx .append( len(TermTopo(r).topoOrder()))
    
    for i in range(13):
        r2 = tr.reduceAll([tr.root])
        lx.append(len(TermTopo(r2).topoOrder()))
        r = r2
        print('final2----\n', pretty(r))
        print('noAtom---\n', pretty(r, noAtom=True))
        print(lx)
        assert r[0] == tr.root
        if lx[-1] >= lx[-2] : break
        pass
    fn  = FuncFoldr.recognize(FuncFoldrPlusM , tr.ht)
    for i in TermTopo(r).topoOrder():
        
        if not FuncFoldrPlusM.accept(i) : continue
        x = fn(i)
        if  not x is None:
            jtag('identify foldr from ', pretty(i))
            jtag('foldr as  ', pretty(x))
            jtag('foldr as (shorted)  ', short(x))
            pass
        if FuncReduceMMS.accept(i):
            jtag("Found MMS", pretty(i))
            jtag("Found MMS", short(i.mms))
            pass
        pass
    d = TermDFS(r[0])
    
    pass
