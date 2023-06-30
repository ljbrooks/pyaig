from autil.lit_util import *
import pdb, pydot
import networkx as nx
default_shape = ''
class DrawAdderTree:
    def __init__(self, ag):
        self.ag = ag
        self.aiger = ag.aiger
        self.acc = ag.acc
        
        self.toDiGraph()
        pass
    def toDiGraph(self):
        self.marked = m = self.compute_marked()
        G = self.G = nx.DiGraph()
        for i in filter(lambda l: m[var(l)] , self.acc.topox):
            g = self.ag.get_matched_gate(i)
            shape = default_shape
            color=self.acc.colorMap[i//2].hash()
            name = self.ag.get_id_name(i) #self.aiger._id_to_name[i] if  i in self.aiger._id_to_name else str(var(i))
            label= '%s/%s'% ( name, self.acc.colorMap[var(i)].cid)
            
            if g:
                i = g.outputx[0]
                G.add_node(var(i),
                           shape = g.shape,
                           penwidth = 2,
                           color = color,
                           label = label
                           )
                
                fx = g 
            else: 
                G.add_node(var(i),
                           penwidth = 4 ,
                           color = color,
                           label = label)
                
                fx = self.acc.aiger.get_fanins(i)
                pass
            for j in fx:
                
                jg = self.ag.get_matched_gate(j)
                edge_label = '' if not jg else jg.get_edge_label(j)    
                j = jg.outputx[0] if jg else j
                G.add_edge(var(j), var(i), style=edge_style(j), 
                           label = edge_label,
                           color = edge_color(j), penwidth =2)
                    
                pass
    
            pass
        self.toDot('x.dot')
        print('x.dot is from DrawAdderTree.py')
        pass
    def toDot(self, fname):

        G = self.G
        p = nx.drawing.nx_pydot.to_pydot(G)

        S =pydot.Subgraph(rank='same')
        pix = [str(i//2) for i in self.aiger.get_pis()]
        for i in pix: S.add_node(pydot.Node(i))
        p.add_subgraph(S)
        k = set(pix)

        poS = set ( self.aiger.get_po_fanins())
        S =pydot.Subgraph(rank='same')
        pix = [str(i//2) for i in self.acc.nodex if self.acc.levelx[var(i)] == 1 and i not in poS and self.marked[var(i)]]
        k = k | set(pix)
        for i in pix: S.add_node(pydot.Node(i))
        p.add_subgraph(S)  

        S =pydot.Subgraph(rank='same')
        
        pox = [str(i//2) for i in self.aiger.get_po_fanins() if str(i//2) not in k]
        for i in pox: S.add_node(pydot.Node(i))
        p.add_subgraph(S)

        print('Gen', fname)
        open(fname, 'w').write(str(p))
        pass
        pass
    def compute_marked(self):
        marked = [False] * self.acc.N
        for i in self.aiger.get_po_fanins(): marked[var(i)] = True
        for i in reversed(self.acc.topox):
            if not marked[var(i)] : continue
            finx = self.ag.get_matched_gate(i) if self.ag.get_matched_gate(i) else self.aiger.get_fanins(i)
            for j in finx: 
                marked[var(j)] = True
            pass
        return marked
    pass
