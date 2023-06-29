import history
from collections import *
import pydot, sys
from pathlib import Path
import random
from colorwheel import ColorWheel
import pyaig
from  natsort import *
sorted = natsorted
from dd.cudd import BDD
import networkx as nx
def var(i) : return i//2
def pure(i): return i ^ (i&0x1)
class Color:
    def __init__(self, cid, rgb):
        self.cid , self.rgb = cid, rgb
        pass
    def hash(self):
        return rgb2hash(self.rgb)
    pass

RED = Color(-1, (255,0,0))
def rgb2hash(args):
    r,g,b = args
    r = ('%x'%r).zfill(2)
    g = ('%x'%g).zfill(2)
    b = ('%x'%b).zfill(2)
    return f'#{r}{g}{b}'

class AigerCoiCluster:
    # cluster is a BDD
    def __init__(self, aiger, rootx = None , stopx= None): 
        self.aiger , self.stopx = aiger, stopx
        if rootx is None: self.rootx = list(aiger.get_po_fanins())        
        self.bddMgr = BDD()
        self.bddMgr.configure(reordering=False)

        self.topox = self.nodex = list(map(pure, aiger.topological_sort(self.rootx)))

        self.N = max(map(lambda i: i//2, self.nodex)) +1
        
        self.levelx = self.compute_level()

        self.coix = [self.bddMgr.false for i in range(self.N)] # as bdd
        self.coix_support = [None] * self.N
        
        self.computer_coix_support_as_bdd()
        self.po_coix = [ self.coix[i//2] for i in self.aiger.get_po_fanins()]
        self.cw = self.get_colorwheel()
        self.colorMap = self.assign_color()
        self.fanout_cnt = self.compute_fanout_count(self.topox)
        pass

    def compute_level(self):
        self.levelx = r = [-1] * self.N
        for i in self.aiger.get_pis(): r[var(i)] = 0
        for i in self.topox:
            for j in self.aiger.get_fanins(i):
                r[var(i)] = max(r[var(i)], r[var(j)]+1)
                pass
            pass
        #print(r)
        # this thing is correct
        return r

    
    def init_pi_color_level(self): # this is a hack, now
        # it is either a multiplier or an ADDer, so hack it, the last
        # one is the carrie bit if it is an adder
        pix = list(self.aiger.get_pis())
        even = lambda i: (i&0x1) ==0
        carry = None
        if not even(len(pix)): carry = pix[-1]
        
        if carry:
            s = str(len(pix)//2+1)
            self.bddMgr.add_var(s)
            self.coix[var(carry)] = self.bddMgr.var(s)
            pass
        
        input_size = len(pix)//2

        # group the adder PI together, actually, there is no need,
        # just assign the order by the inputs, then it is fine.

        for k, (i,j) in enumerate(list(zip(pix[:input_size], pix[input_size: input_size*2]))):
            # this is the paried bits
            self.bddMgr.add_var(str(k))
            self.coix[var(i)] = self.bddMgr.var(str(k))
            self.coix[var(j)] = self.bddMgr.var(str(k))
            pass
        
        pass
    def computer_coix_support_as_bdd(self):
        self.init_pi_color_level()
        for i in self.nodex:
            v = var(i)
            if  self.aiger.is_const0(i):
                self.coix[v] = self.bddMgr.false
            #elif self.levelx[v]<=1:
            elif self.aiger.is_pi(i):
                
                #self.bddMgr.add_var(str(v)) # this needs be reconsidered
                #self.coix[v] = self.bddMgr.var(str(v))
                continue
                pass
            else:
                for j in self.aiger.get_fanins(i):
                    jvar = var(j)
                    self.coix[v] = self.coix[v] | self.coix[jvar]
                    pass
                pass
            pass

        pass
    def computer_coix_support_as_bdd_old(self):
            
        for i in self.nodex:
            var = i//2
            if self.aiger.is_pi(i):
                self.bddMgr.add_var(str(var))
                self.coix[var] = self.bddMgr.var(str(var))
                pass
            elif self.aiger.is_const0(i):
                self.coix[var] = self.bddMgr.false
            else:
                for j in self.aiger.get_fanins(i):
                    jvar = j//2
                    self.coix[var] = self.coix[var] | self.coix[jvar]
                    pass
                pass
            pass
        pass
    def compute_base_cluster(self):
        #  not used
        pox = natsorted(self.po_coix, key= lambda i: (len(i), natsorted(i.support)))
        yield pox[0]
        print('result', pox[0].support)
        for i,j in zip(pox[:-1], pox[1:]):
            print(i.support)
            print(j.support)
            x =self.bddMgr.cofactor(j, ~i)
            print('result', x.support)
            yield x
            pass
        pass
    
    def compute_fanout_count(self, topoListOfNodes):
        fanout_cnt = [0] * max(map(var, topoListOfNodes) ) +[0]
        for i in topoListOfNodes:
            for j in self.aiger.get_fanins(i):
                fanout_cnt[var(j)] += 1
                pass
            pass
        return fanout_cnt
    
    def assign_color(self):
        
        s = set(filter( lambda i: len(i.support)>1, self.coix))

        #print('len s', len(s))
        sx = [str(natsorted(i.support)) for i in self.coix]
        sx = list(natsorted(set(sx)))
        
        r =   defaultdict(lambda : RED, dict(zip(sx,self.cw)))
        for i,j in r.items():
            #print(i, j.cid, j.rgb, j.hash())
            pass
        #print([type(i) for i in r])
        cx = [ natsorted(i.support) for i in s if not isinstance (i,str)]
        #print('supportx')
        #print(cx)
        cx = [r[str(natsorted(i.support))] for i in self.coix]
        #print(cx)
        for i , j in zip(self.coix, cx):
            #print(i.support, j)
            pass
        return cx

    def get_colorwheel(self):
        #s = set(filter( lambda i: len(i.support)>1, self.coix))
        sx = [str(natsorted(i.support)) for i in self.coix]
        sx = list(natsorted(set(sx)))
        s = sx
        n = len(s)

        n = n//12 * 12 if n %3 == 0 else n//12*12 + 12
        #print(n)
        cw = ColorWheel(color_number = n)
        
        cw = list(map(lambda i: Color(*i), enumerate( cw.colors)))
        
        # random.seed(0)
        # random.shuffle(cw)
        return cw
    def toDiGraph(self):
        G = nx.DiGraph()
        for i  in self.nodex:
            G.add_node(i//2, 
                       color=self.colorMap[i//2].hash() , 
                       label= '%s/%s'% ( var(i), self.colorMap[var(i)].cid),
                       #label= '%s'% (self.colorMap[i//2].cid) if self.levelx[var(i)]>1 else  '%s/%s'% ( i//2, self.colorMap[i//2].cid),
                       penwidth = 2
                       )
            pass
        for i in self.nodex:
            for j in self.aiger.get_fanins(i):
                G.add_edge(j//2, i//2, style="" if j&0x1 == 0 else "dotted")
                pass
            pass

        return G
    def toDot(self, fname):
        G = self.toDiGraph()
        p = nx.drawing.nx_pydot.to_pydot(G)
        S =pydot.Subgraph(rank='same')
        pix = [str(i//2) for i in self.aiger.get_pis()]
        for i in pix: S.add_node(pydot.Node(i))
        p.add_subgraph(S)

        poS = set ( self.aiger.get_po_fanins())
        S =pydot.Subgraph(rank='same')
        pix = [str(i//2) for i in self.nodex if self.levelx[var(i)] == 1 and i not in poS]
        for i in pix: S.add_node(pydot.Node(i))
        p.add_subgraph(S)

        S =pydot.Subgraph(rank='same')
        pix = [str(i//2) for i in self.aiger.get_po_fanins()]
        for i in pix: S.add_node(pydot.Node(i))
        p.add_subgraph(S)
        open(fname,'w').write(str(p))
        pass
    pass
if __name__ == '__main__':



   f = '/home/long/uu/pyaig/benchmarks/iscas-89/blif/c6288.aig'
   f = '/home/long/uu/multgen/s.aig'

   

   f = '/home/long/uu/pyaig/benchmarks/iscas-89/blif/c6288.aig'
   fx = '''s1.aig s.aig s2.aig mock/d.aig mock/c.aig m4.aig
/home/long/uu/multgen/c42_USP_KS_4x4_noX_multgen.sv.aig
'''.split() 
   #   fx = 's2.aig'.split()
   if len(sys.argv[1:]) > 0: fx = sys.argv[1:]
   for f in fx:
       
       a = pyaig.aig_io.read_aiger(f)
       acc = AigerCoiCluster(a)
       bx = set(acc.coix)
       bx = [natsorted(i.support) for i in bx]
       bx = natsorted(bx, key = lambda i: (len(i), i))
       #list(map(print, bx))
       
       print('pox')
       po_coix = [natsorted(i.support) for i in acc.po_coix]
       
       #list(map(print, po_coix))
       
       u = list(acc.compute_base_cluster())
       u = filter(lambda i: len(i.support)>0, u)
       #print(list(map(lambda i: i.support, u)))
       # compute coloring
       cw = acc.assign_color()
       
       outfname = str(Path(f).name[:-4] )+ '.dot'
       G = acc.toDot(outfname)
       #nx.drawing.nx_pydot.write_dot(G,outfname)
       print('Gen', outfname, 'from', f)
       pass
   
