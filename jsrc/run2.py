from scr.TermTopo import *
import pdb
from scr.TermDot import *
from scr.TermMgr import *
from scr.TermBuilder import *
from scr.TermRewriter import *
from scr.TermReduce2 import *
from scr.TermDFS import *
from scr.TermHorner import *
from scr.TermSOP import *
import math
from tabulate import *
from scr.util import *
from jtag3 import jtag as jjtag
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
jjtag("original", pretty(pox[0]))
ux = pox
for u in ux:
    x = rewrite(u, a)
    pass

rx = [rewrite(i, a) for i in pox]
jjtag("after first rewrite", pretty(rx[-1]))
"""
for i in pox:
    pdb.set_trace()
    u = rewrite(i,a)
    print(u)
"""

def Open(fname, mode):
    m = {"w": "write", "r": "read", "a": "append"}
    print(f"INFO: file {m[mode]} : {fname} {mode}")
    return open(fname, mode)

for i in rx:
    lx = [len(TermTopo(i).topoOrder())]
    tr = TermReduce2(i)
    r = tr.root
    lx.append(len(TermTopo(r).topoOrder()))

    # for i in range(20):
    while True:
        r2 = tr.reduceAll([tr.root])
        lx.append(len(TermTopo(r2).topoOrder()))
        r = r2
        print("final2----\n", pretty(r))
        Open("final2.txt", "w").write(pretty(r))
        Open("final2_noAtom.txt", "w").write(pretty(r, noAtom=True))
        print("noAtom---\n", pretty(r, noAtom=True))
        print(lx)
        assert r[0] == tr.root
        if lx[-1] == lx[-2]:
            break
        pass
    # break
    
    fn = FuncFoldr.recognize(FuncFoldrPlusM, tr.ht)
    
    for i in TermTopo(r).topoOrder():
        if not FuncFoldrPlusM.accept(i):
            continue
        x = fn(i)
        if not x is None:
            jtag("identify foldr from ", pretty(i))
            jtag("foldr as  ", pretty(x))
            jtag("foldr as (shorted)  ", short(x))
            pass
        if FuncReduceMMS.accept(i):
            jtag("Found MMS", pretty(i))
            jtag("Found MMS", short(i.mms))
            pass
        
        if i.uid in [216 , 236] and TermWideNOR.accept(i):
            s =  TermWideNOR.recognize(i)
            assert isA(ExprInv)(s) and isA(FuncWideOR) (s.car)
            jjtag("Found TermWideNOR",str(fmap(ustr, [s.car.root, s.car.mids, s.car.termx]) ))
            for j in s.car.termx:
                if tsign(j): j = j.car
                rr = collect_wide_and(j)
                jjtag("Found TermWideAnd",str(fmap(ustr, [rr.root, rr.mids, rr.termx]) ))
                pass
            #print(i.wnor)
            assert isA(ExprInv)(i.wnor)
            assert isA(FuncWideOR)(i.wnor.car)
            expand_wide_or(i.wnor.car)
            pass
        
        pass
    
    d = TermDFS(r[0])

    jjtag("short2", str(short2(r[0])))
    Open("short2.txt", "w").write(short2(r[0]))
    rh = ReduceSOP(tr.ht)
    t = rh.reduce_r(r[0])
    jjtag('SOP-reduced', pretty(t))
    t = ReduceHorner(tr.ht).reduce(t)
    jjtag('horner-reduced', pretty(t))
    
    pass
