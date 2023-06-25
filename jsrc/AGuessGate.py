import pyaig
import pdb
import networkx as nx
from AigerCoiCluster import *
from AGate import *
from autil.lit_util  import *
class AGuessGate:
    
    def __init__(self, aiger, rootx=None):
        self.aiger , self.rootx = aiger, rootx
        if rootx is None: self.rootx = list(aiger.get_po_fanins())

        self.acc = AigerCoiCluster (aiger, rootx)
        self.gatex = [ [] for i  in range(self.acc.N)]

        self.ppx = self.identify_first_layer_pp()
        XOR_FIRST = False
        for i in self.acc.topox:
            if var(i) == 92:
                print('special')
                self.print_gate(i)
                pass
            assert not sign(i)
            if not XOR_FIRST : self.extend_and(i)
            if self.acc.levelx[var(i)] >=2:
                self.identify_xor(i)
                pass
            if XOR_FIRST : self.extend_and(i)
            pass
        
        pass

    def identify_first_layer_pp(self):
        ret = [None] * self.acc.N
        level1 = filter(lambda i: self.acc.levelx[var(i)] ==1, self.acc.topox)
        px = filter(lambda i: self.is_pp(i) , level1)
        for i in px:
            ret[var(i)] = AGate_PP(self.aiger.get_fanins(i), i)
            print('PP')
            self.print_gate0(i)
            pass
        return ret
    def is_pp(self, i):
        l , r = self.aiger.get_fanins(i)
        if not sign(l) and not sign(r): return True
        
        pass
    
    def rewrite_based_on_color_ordering(self):
        # create a new aiger based on this
        
        pass

    def compute_marked(self):  
        # this is the set to be reordered and then create another AIGER based on this
        self.marked = marked = [False] * self.acc.N
        for i in self.acc.aiger.get_po_fanins():
            marked[var(i)] = True
            pass
        for i in reversed(self.acc.topox):
            if not marked[var(i)] : continue
            gx = self.gatex[var(i)]
            if len(gx) == 0:
                for j in map(var, self.acc.aiger.get_fanins(i)):
                    marked[j] = True
                    pass
                pass
            else:
                #print(gx, i)
                fanin = gx[0] # .covered_litx[1] # 
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
                           penwidth = 4 if not self.ppx[var(i)] is None else 2,
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
    def print_gate0(self,lit):
        l,r = self.aiger.get_fanins(lit)
        print(f'{var(lit)} := {var(l)} AND {var(r)}')
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
        if self.acc.levelx[var(lit)]<=1: return # skip

        kx = list(self._extend_and_r(lit))
        kkx = [i[1] for i in kx if i[0] == 1]
        mx = [i[1] for i in kx if i[0] == 0]
        if len(kkx)>2:
            print('found wide and%s @%s = AND %s'% (len(kx), var(lit), 
                                                    list(map(lambda i: (i[0], lstr(i[1])),kx))))
            a = AGate_AND( kkx, [lit], mx)
            self.gatex[var(lit)].append(a)
            
            if len(kkx) == 3:
                #if var(lit) == 86: pdb.set_trace()
                    
                r = AGate_Majority3.identify(self.aiger, a)
                if not r is None:
                    #assert False
                    self.gatex[var(lit)] = [r] + self.gatex[var(lit)]
                    pass
                pass
            pass
        pass
    def _extend_and_r(self, lit):
        if len(self.gatex[var(lit)] )>0 and not isinstance(self.gatex[var(lit)][0], AGate_AND):
            yield 1,lit
            return 
        if self.acc.levelx[var(lit)]<=1: 
            #yield (1, lit)      # boundary at level 1
            #return 
            pass
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
        G = None
        if sign(l) and sign(r) and inv(l_fanin) == r_fanin:
            G = AGate_XOR
        elif sign(l) and sign(r) and inv(l_fanin) == r_fanin:
            # not used
            G = AGate_NXOR
            pass
        if not G is None:
            self.gatex[var(lit)].append(G([inv(r_fanin[0]), r_fanin[1]], lit, 
                                        ([l,r]), # 
                                        ))
                                        
            print('found ', var(lit), '%s = %s %s %s' % ( var(lit), 
                                                          lstr(inv(r_fanin[0])), 
                                                          G.name,
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




    f = 'mock/c.aig'
    f = 'mock/d.aig'
    f = '../../multgen/HC_8_multgen.sv.aig'
    f = 'KS_8_multgen.sv.aig'
    f = '/home/long/uu/multgen/c42_USP_KS_4x4_noX_multgen.sv.aig'
    f = 'WT_USP_KS_8x8_noX_multgen.sv.aig'
    f = 'b16.aig'

    f = 'mock/d.aig'
    f = '/home/long/BK_15_15.aig'
    f = '/home/long/WT.aig'
#    f = 'kk.aig'
#    f = 'ka.aig'
#    f = 'k.aig'
    #f = 'mock/c.aig'
    #f = 'mock/e.aig'
    a = pyaig.aig_io.read_aiger(f)
    ag = AGuessGate(a)
    outfname = str(Path(f).name[:-4] )+ '.dot'
    G = ag.acc.toDot(outfname)
    print('gen gussed dot:', 'v.dot')
    ag.toDot('v.dot')