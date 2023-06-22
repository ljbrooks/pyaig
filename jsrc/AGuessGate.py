import pyaig
import networkx as nx
from AigerCoiCluster import *
from AGate import *
def var(i) : return i//2
def lstr(i): return '%s%s'% ('+-'[sign(i)],var(i))
def sign(lit): return (lit &0x1) == 1
def ssign(lit): return '+-'[int(sign(lit))]
def inv(lit) : 
    if isinstance(lit, int):
        return lit ^ 0x1
    assert isinstance(lit, list)
    return list(map(inv, lit))
def pure(i): return i ^ (i&0x1)
def edge_style(i):
    return 'dotted' if sign(i) else ""
def edge_color(i):
    return 'blue' if sign(i) else ""
class AGuessGate:

    def __init__(self, aiger, rootx=None):
        self.aiger , self.rootx = aiger, rootx
        if rootx is None: self.rootx = list(aiger.get_po_fanins())
        self.acc = AigerCoiCluster (aiger, rootx)
        self.gatex = [ [] for i  in range(self.acc.N)]
        for i in self.acc.topox:
            assert not sign(i)
            self.extend_and(i)
            if self.acc.levelx[var(i)] >=2:
                self.identify_xor(i)
                pass
            
            pass
        pass
    def compute_marked(self):
        marked = [False] * self.acc.N
        for i in self.acc.aiger.get_po_fanins():
            marked[var(i)] = True
        for i in reversed(self.acc.topox):
            if not marked[var(i)] : continue
            gx = self.gatex[var(i)]
            if len(gx ) == 0:
                for j in map(var, self.acc.aiger.get_fanins(i)):
                    marked[j] = True
                    pass
                pass
            else:
                print(gx, i)
                g = gx[0]
                fanin = g # .covered_litx[1] # 
                for k in map(var, fanin): marked[k] = True
                pass
            pass
        return marked

    def toDiGraph(self):
        m = self.compute_marked()
        G = nx.DiGraph()
        for i in self.acc.topox:
            if not m[var(i)] : continue # skip
            shape = ''
            color=self.acc.colorMap[i//2].hash() 
            label= '%s/%s'% ( var(i), self.acc.colorMap[var(i)].cid)
            if len( self.gatex[var(i)]) > 0: 
                g = self.gatex[var(i)][0] #.covered_litx[1]

                G.add_node(var(i), 
                           shape = g.shape,
                           penwidth = 2, 
                           color = color,
                           label = label
                           ) 
                fx = g
            else:
                G.add_node(var(i), 
                           penwidth = 2,
                           color = color,
                           label = label)
                fx = self.acc.aiger.get_fanins(i)
                pass
            for j in fx:
                G.add_edge(var(j), var(i), style=edge_style(j), color = edge_color(j))
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
        pix = [str(i//2) for i in self.acc.nodex if self.acc.levelx[var(i)] == 1 and i not in poS]
        for i in pix: S.add_node(pydot.Node(i))
        p.add_subgraph(S)  

        S =pydot.Subgraph(rank='same')
        pix = [str(i//2) for i in self.aiger.get_po_fanins()]
        for i in pix: S.add_node(pydot.Node(i))
        p.add_subgraph(S)

        print('Gen', fname)
        open(fname, 'w').write(str(p))
        pass
    def print_gate(self,lit):
        l = self.aiger.get_and_left(lit)
        r = self.aiger.get_and_right(lit)
        ll = self.aiger.get_and_left(l)
        lr = self.aiger.get_and_right(l)
        rl = self.aiger.get_and_left(r)
        rr = self.aiger.get_and_right(r)
        
        r = '%s = %s( %s & %s ) & %s( %s & %s)' % (lstr(lit), 
                                                   ssign(l),
                                                   lstr(ll),
                                                   lstr(lr),
                                                   ssign(r),
                                                   lstr(rl),
                                                   lstr(rr))
        print(r)
        pass
    def extend_and(self, lit):
        kx = list(self._extend_and_r(lit))
        kkx = [i[1] for i in kx if i[0] == 1]
        mx = [i[1] for i in kx if i[0] == 0]
        if len(kkx)>2:
            print('found wide and%s @%s = AND %s'% (len(kx), var(lit), 
                                                    list(map(lambda i: (i[0], lstr(i[1])),kx))))
            self.gatex[var(lit)].append(AGate_AND( kkx, [lit], mx))
                                                  
            pass
        pass
    def _extend_and_r(self, lit):
        if sign(lit): 
            yield (1, lit)
            return 
        if len(self.aiger.get_fanins(lit))!= 2: 
            yield (1, lit)
            return 
        #l,r = self.aiger.get_fanins(lit)
        for i in self.aiger.get_fanins(lit):
            for x, j in self._extend_and_r(i):
                yield (x, j)
                pass
            pass
        yield(0,lit)
        pass
    def identify_xor(self, lit):
        assert len(list(self.aiger.get_fanins(lit))) == 2
        l = self.aiger.get_and_left(lit)
        r = self.aiger.get_and_right(lit)
        l_fanin = sorted(list(self.aiger.get_fanins(l)))
        r_fanin = sorted(list(self.aiger.get_fanins(r)))
        if sign(l) and sign(r) and inv(l_fanin) == r_fanin:
            self.gatex[var(lit)].append(AGate_XOR([inv(r_fanin[0]), r_fanin[1]], lit, 
                                        ([l,r]), # 
                                        ))
                                        
            print('found ', var(lit), '%s = %s XOR %s' % ( var(lit), 
                                                           lstr(inv(r_fanin[0])), 
                                                           lstr(r_fanin[1])
                                                          ))
            self.print_gate(lit)
            
            return True
        else:
            return False
        pass
    pass
if __name__ == '__main__':


    f = 'm4.aig'

    f = '/home/long/uu/multgen/c42_USP_KS_4x4_noX_multgen.sv.aig'


    f = 'mock/c.aig'
    f = 'mock/d.aig'
    #f = 'mock/e.aig'
    a = pyaig.aig_io.read_aiger(f)
    ag = AGuessGate(a)
    outfname = str(Path(f).name[:-4] )+ '.dot'
    G = ag.acc.toDot(outfname)
    ag.toDot('u.dot')
