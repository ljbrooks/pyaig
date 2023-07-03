from scr.TermTopo import *
import pdb
from scr.TermDot import *
from scr.TermMgr import *
from scr.TermBuilder import *
from scr.TermRewriter import *
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


print(tabulate([[i.nid, str(i)] for i in topo.topoOrder()]))


a = TermRewriter()

#pdb.set_trace()
#u= rewrite(xs80,a)

#ux = [xs156] #xs86, xs44, xs150, xs156]
ux = pox
for u in ux:
    print
    x= rewrite(u,a)
    print('before --')
    print(pretty(u))
    print('after-----')
    print(pretty(x))
    print()
print(str(u))

'''
for i in pox:
    pdb.set_trace()
    u = rewrite(i,a)
    print(u)
'''
