from scr.TermTopo import *
import pdb
from scr.TermDot import *
from scr.TermMgr import *
from scr.TermBuilder import *
from scr.TermRewriter import *
from scr.TermReduce import *
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


# print(tabulate([[i.nid, str(i)] for i in topo.topoOrder()]))


a = TermRewriter()

# pdb.set_trace()
# u= rewrite(xs80,a)

# ux = [xs156] #xs86, xs44, xs150, xs156]
print(pretty(pox[0]))
ux = pox
rx = [rewrite(i, a) for i in pox]
print("after rewrite")

print(pretty(rx[0]))
# exit(0)
"""
for i in pox:
    pdb.set_trace()
    u = rewrite(i,a)
    print(u)
"""


for i in rx:
    t = TermTopo(rx[0])
    old = len(t.topoOrder())
    tr = TermReduce(i)
    #    print(tr.x)
    for x in tr.x:
        # print('uid:', x.uid)
        # print(pretty(x))
        # print(f'%s'% ( [j.uid for j in x.termx]), ' -- ' , x.termx.uid)
        pass
    t = TermTopo(tr.x[-1])
    l2 = len(t.topoOrder())
    print("length change", old, len(t.topoOrder()))
    r = tr.reduce(tr.x[-1])
    # r = tr.x[-1]#t.topoOrder()[-1]
    t = TermTopo(r)

    print("final", pretty(r))
    print("length change", old, l2, len(t.topoOrder()))
    lx = [0, old, l2, len(t.topoOrder())]
    for i in range(20):
        r2 = tr.reduceAll(r)
        lx.append(len(TermTopo(r2).topoOrder()))
        r = r2
        print("final2----\n", pretty(r))
        # print('length change2', old, l2, len(t.topoOrder()))

        print("noAtom---\n", pretty(r, noAtom=True))
        print(lx)

        if lx[-1] == lx[-2] and lx[-2] == lx[-3]:
            break
        pass
    print(lx)
    d = TermDFS(r)

    pass
