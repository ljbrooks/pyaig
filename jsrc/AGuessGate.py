import sys
sys.path.append('../')
import pyaig
from collections import *
import pdb
import networkx as nx
from AigerCoiCluster import *
from AGate import *
from autil.lit_util  import *
from DrawAdderTree import *
import pyaig
class VarMap(dict):
    def __init__(self):
        pass
    pass
def iter(a):
    if isinstance(a,VarMap):
        return sorted(a.items(), key=lambda i:i[0])
    pass
class AGuessGate:
    def __init__(self, aiger, rootx=None):
        if isinstance(aiger, str) : aiger = pyaig.aig_io.read_aiger(aiger)
        self.aiger , self.rootx = aiger, rootx
        if rootx is None: self.rootx = list(aiger.get_po_fanins())

        self.acc = AigerCoiCluster (aiger, rootx)
        self.gatex = [ [] for i  in range(self.acc.N)]

        self.ppx = self.identify_first_layer_pp() # prefix
        self.xor3x = defaultdict(list)
        self.inverse_xor3 = defaultdict(list)
        self.HAx = defaultdict(list)
        self.FAx = defaultdict(list)
        self.guess_gates()
        self.first_level_xor3=VarMap()
        self.draw_adder_tree()
        pass
    def is_xor(self, i):
        return len(self.gatex[var(i)])>0 and isinstance(self.gatex[var(i)][0], AGate_XOR)
    def get_xor(self, i):
        return self.gatex[var(i)][0]
    def get_gate(self, i, gate_type, force = True):
        f = self.gatex[var(i)]
        if not force and not f: return None
        if not isinstance(f, gate_type) and not force: return None
        r=  self.gatex[var(i)][0]
        self.is_gate(i, gate_type)
        return r
    def get_matched_gate(self,i):
        get = lambda lx: lx[var(i)][0] if var(i) in lx else None
        lxx = [self.FAx, self.HAx]
        for lx in lxx: 
            g = get(lx) 
            if g: return g
            pass
        if self.gatex[var(i)]: return self.gatex[var(i)][0]
        return None
    def get_HA(self, i):        
        return None  if not var(i) in self.HAx else self.HAx[var(i)]
    def get_FA(self, i):        
        return None  if not var(i) in self.FAx else self.FAx[var(i)]

    
    def is_gate(self, i, gate_type):
        return len(self.gatex[var(i)])>0 and isinstance(self.gatex[var(i)][0], gate_type)
    def show_gate(self, i):
        for j in self.gatex[var(i)]:
            print(f'var@{var(i)}: ', j.__class__.__name__, j)
            pass
    def guess_gates(self):
        XOR_FIRST = False
        for i in self.acc.topox:
            if var(i) == 92:
                print('special')
                #self.print_gate(i)
                pass
            assert not sign(i)
            if not XOR_FIRST : self.extend_and(i)
            if self.acc.levelx[var(i)] >=2:
                self.identify_xor(i)
                pass
            if XOR_FIRST : self.extend_and(i)
            pass
        scanned = defaultdict(set)
        for i in reversed(self.acc.topox):
            if var(i) not in scanned[str(AGate_XOR)] and self.is_xor(i):
                root, faninx, internalx = AGate_XOR_chain.identify(self, i)
                scanned[str(AGate_XOR)].union( set(map(var, internalx)))
                pass
            self.scan_for_chain( i, AGate_Majority3, scanned[str(AGate_Majority3)])
            pass
        print(scanned)
        AGate_XOR3.identify(self)
        AGate_FA.identify(self)
        AGate_HA.identify(self)
        pass
    def scan_for_chain(self, i, gate_type, scanned):
        if self.is_gate(i, gate_type) and not var(i) in scanned:
            f, faninx, internalx = Identify_chain(self, i,gate_type)
            scanned .union(set(map(var, internalx)))
            pass
        pass
    def identify_first_layer_pp(self):
        ret = [None] * self.acc.N
        level1 = filter(lambda i: self.acc.levelx[var(i)] ==1, self.acc.topox)
        px = filter(lambda i: self.is_pp(i) , level1)
        for i in px:
            ret[var(i)] = AGate_PP(self.aiger.get_fanins(i), [i], [])
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

    def get_id_name(self, i):
        if i in self.aiger._id_to_name:
            return self.aiger._id_to_name[i].decode('utf-8')
        else:
            return str(var(i))
    
    def toDiGraph(self):
        m = self.compute_marked()
        G = nx.DiGraph()
        for i in self.acc.topox:
            if not m[var(i)] : continue # skip
            shape = ''
            color=self.acc.colorMap[i//2].hash() 
            name = self.get_id_name(i) #self.aiger._id_to_name[i] if  i in self.aiger._id_to_name else str(var(i))
            label= '%s/%s'% ( name, self.acc.colorMap[var(i)].cid)

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
                G.add_edge(var(j), var(i), style=edge_style(j), color = edge_color(j), penwidth =2)
                pass
            for i, (_, po_lit, po_name) in enumerate(self.aiger.iter_po_names()):
                n = po_name.decode('utf-8')
                G .add_node(n,
                            penwidth = 6)
                G.add_edge(var(po_lit), n, 
                           style= edge_style(po_lit),
                           color = edge_color(po_lit)
                           )
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

        # _, po_lit, po_name for i in list(self.aiger.iter_po_names()

        print('AGuessGate Gen', fname)
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
                    self.gatex[var(lit)] = [r] + self.gatex[var(lit)] # majority is first one
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
            assert False
            G = AGate_NXOR
            pass
        if not G is None:
            finx = r_fanin if not sign(r_fanin[0]) else l_fanin
            xor = G(finx,
                    [lit],
                    [l,r], # 
                    )
            # nxor gate
            xor.is_nxor = sign(r_fanin[0]) != sign(r_fanin[1])
            self.gatex[var(lit)].append(xor)
            
            print('found ', var(lit), '%s = %s %s %s' % ( var(lit), 
                                                          lstr(xor[0]),
                                                          G.name,
                                                          lstr(xor[1])
                                                          ))
            self.print_gate(lit)
            
            return True
        else:
            return False
        pass
    def draw_adder_tree(self):
        d = DrawAdderTree(self)
        pass
    pass
if __name__ == '__main__':


    f = 'm4.aig'




    f = 'mock/c.aig'
    f = 'mock/d.aig'
    f = '../../multgen/HC_8_multgen.sv.aig'

    f = '/home/long/uu/multgen/c42_USP_KS_4x4_noX_multgen.sv.aig'

    f = 'b16.aig'

    f = 'mock/d.aig'
    f = '/home/long/BK_15_15.aig'
    f = '/home/long/WT.aig'
    f =  '../benchmarks/iccad-2022-prob-A/links/pa_03.aig'
    f = 'WT_USP_KS_8x8_noX_multgen.sv.aig'
    f = '/home/long/uu/genmul/8_8_U_SP_WT_KS_GenMul.v.aig'
#    f = '/home/long/uu/pyaig/benchmarks/RitircBiereKauers-DATE18-data/benchmarks/aoki/sp-ar-cl-8.aig'

#    f = 'kk.aig'
#    f = 'ka.aig'
#    f = 'k.aig'
    #f = 'mock/c.aig'
    #f = 'mock/e.aig'
    from filex import f
    if len(sys.argv)>1: f = sys.argv[1]
    a = pyaig.aig_io.read_aiger(f)
    ag = AGuessGate(a)
    outfname = str(Path(f).name[:-4] )+ '.dot'
    G = ag.acc.toDot(outfname)
    print('gen gussed dot:', 'v.dot')
    ag.toDot('v.dot')
    pass
