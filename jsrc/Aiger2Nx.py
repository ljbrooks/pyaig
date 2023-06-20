import networkx as nx
import pyaig

class Aiger2Nx:
    
    
    pass


class AigerGraph:
    def __init__(self, aiger):
        self.aiger = aiger
        self.G = nx.DiGraph()
        self.G2 = nx.Graph()
        self.G3 = nx.DiGraph()

        self.build_graph()

        pass

    def build_graph(self):
        
        a = self.aiger
        for i in self.aiger.get_and_gates():
            ii = i//2
            l = a.get_and_left(i) //2
            r = a.get_and_right(i) //2
            self.G.add_edge(l,i//2)
            self.G.add_edge(r,i//2)
            
            self.G2.add_edge(i//2, l)
            self.G2.add_edge(i//2, r)
            self.G3.add_edge(i//2, l)
            self.G3.add_edge(i//2, r)
            pass
        return 
    
    pass
