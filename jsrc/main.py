import pyaig
from dd.cudd import BDD
import networkx as nx
from Aiger2Nx import *
from Aiger2Bdd import *
import glob
f = '../../benchmarks/arithmetic/adder.aig'
f = '/home/long/uu/aiger/examples/and.aig'
f = '/home/long/uu/pyaig/benchmarks/iscas-89/blif/c432.aig'
f = '/home/long/uu/pyaig/benchmarks/iscas-89/blif/c880.aig'
f = '/home/long/uu/pyaig/benchmarks/iscas-89/blif/c7552.aig'
a = None
def build_bdd(f):
    global a
    a = pyaig.aig_io.read_aiger(f)
    
    g = AigerGraph(a)
    

    pr = nx.pagerank(g.G,alpha=0.9)
    
    px = sorted(pr.items(), key=lambda i: i[1])

    nx.drawing.nx_pydot.write_dot(g.G,'a.dot')

    u = nx.voterank(g.G,32)
    
    u2 = nx.voterank(g.G2,32)

    tx = list(a.topological_sort(a.get_po_fanins()))
    
    abd = Aiger2Bdd(a)
    
    #abd.build_bdd(tx)
    print(abd.bddMgr.statistics())
    return a, g, u, u2, tx

def build_from_dir(d):
    ax = glob.glob(f'{d}/c*.aig')
    for i in ax:
        if i.find('6288') == -1: continue
        print('build', i)
        r = build_bdd(i)
        pass
    return r
if __name__ == '__main__':
    
    d = '/home/long/uu/pyaig/benchmarks/iscas-89/blif/'
    r = build_from_dir(d)
    a, g, u, u2, tx = r
    pass
