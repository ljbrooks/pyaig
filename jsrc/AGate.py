from collections import *
import pdb, pydot
from natsort import *
from functools import *
from autil.lit_util import *
class AGate(list):
    def __init__(self, inputx, outputx, covered_litx):
        list.__init__(self, inputx)
        self.covered_litx = covered_litx
        self.outputx = outputx
        assert isinstance(outputx, list)

        pass
    @property
    def internal_gate_cnt(self):
        return len(self.covered_litx)
    def identify(self, lit):  assert False
    def get_edge_label(self, i) : return ''
    pass
class AGate_OR(AGate):
    name = 'OR'
    shape = 'plain'
    pass
class AGate_AND(AGate):
    name = 'AND'
    shape = 'rectangle'
    pass
class AGate_XOR(AGate):
    shape = 'diamond'
    name = 'XOR'
    pass

class AGate_NXOR(AGate):
    shape = 'pentagon'
    name = 'NXOR'
    pass

class AGate_PP(AGate):          # partial-product
    shape = 'dot'
    name = 'PP'
    pass

class AGate_XOR_chain(AGate):
    shape = 'Mdiamond'
    name = 'xor_chain'

    @staticmethod
    def identify ( acc,  xor):
        assert isinstance(acc.gatex[var(xor)][0], AGate_XOR)
        lx = list( AGate_XOR_chain._identify_r(acc, pure(xor)))
        faninx = list(filter(lambda i: i[1] == 0, lx))
        internalx = list(filter(lambda i: i[1] == 1, lx))
        faninx , _  = zip(*faninx)
        internalx , _ =  zip(*internalx)
        if len(lx) > 3: 
            print("Found xor_chain:", f"{var(xor)} = %s" % (" XOR ".join(map(lstr,faninx))))
            pass
        return xor, faninx, internalx
    
    @staticmethod
    def _identify_r ( acc, xor):
        #        if var(xor) == 81: pdb.set_trace()
        if not acc.is_xor(xor) : 
            yield xor, 0        # a leaf
        else:
            for input in acc.get_xor(xor):
                for i in AGate_XOR_chain._identify_r(acc, input):
                    yield i
                    pass
                pass
            yield xor, 1        # not a leaf
            pass
        pass
    pass

#is_xor = lambda a: isinstance(a, AGate_XOR) or isinstance(a, AGate_XOR_chain)

class AGate_Majority3(AGate):          # majority function
    shape = 'box3d'
    name = 'maj3'
    @staticmethod
    def identify ( aiger, and3):
        assert isinstance(and3, AGate_AND)
        f = and3.outputx[0]     # f is the output
        ixx = list(map(lambda i: aiger.get_fanins(i), and3)) # get the trans fanins
        i2x = list(set(sum(ixx,[])))
        if len(i2x)!= 3 : return None                   # should be 3 different fanins
        c= Counter(sum(ixx,[]))
        if [i[1] for i in c.items()] != [2]*3 : return None # each appears twice
        b = map(lambda i: i[0] != i[1], ixx)                 # none should appeared under 1,
        if sum(b) != 3: return False

        print(inv(i2x))
        #assert False
        return AGate_Majority3( inv(i2x), # invert the majority
                                [f],
                                and3)
    pass
class AGate_XOR3(AGate):
    shape = 'invtriangle'
    name = 'xor3'
    @staticmethod
    def identify (ag):
        is_xor = lambda i: ag.is_gate(i, AGate_XOR)        
        for i in ag.acc.topox:
            if is_xor(i): AGate_XOR3._identify(ag,i)
            pass

        pass

    @staticmethod
    def _identify (ag, i):
        
        is_xor = lambda i: ag.is_gate(i, AGate_XOR)        
        assert is_xor(i)
        gate = ag.get_gate(i, AGate_XOR)
        assert len(gate) == 2
        for fanin in gate:
            other = [x for x in gate]
            other.remove(fanin)
            assert len(other) == 1
            if is_xor(fanin):
                ix = ag.get_gate(fanin, AGate_XOR)
                r=  AGate_XOR3(ix + other, [i], [fanin])
                if sign(fanin): inv_one(r) # invert one of the outputs 
                ag.xor3x[var(i)].append(r)
                ag.inverse_xor3[str(natsorted(pure(r)))].append(r)
                print(list(ag.inverse_xor3.items())[:10])
                print(f'insert {var(i)} ', str(natsorted(list(map(lstr, r)))))
                print(f'found xor3  {var(i)} := %s' % ' ^ '.join(map(lstr,r)))
                pass
            pass
        pass


class AGate_FA(AGate):
    shape = 'trapezium'
    name = 'FA'
    edge_label = ['xor','maj']
    def is_sum_bit(self, i):
        return i == self[1]
    def is_carry_bit(self, i):
        return i == self[0]
    def get_edge_label(self, i):
        return self.edge_label[ var(i) == var(self.outputx[0])]    
    @staticmethod
    def identify(ag):
        # i needs be a majority node
        for i in ag.acc.topox:
            #if var(i) == 85: pdb.set_trace()
            if ag.is_gate(i, AGate_Majority3):
                node = ag.get_gate(i, AGate_Majority3)
                ss = natsorted(pure(node))
                print('try',var(i), ss)
                if str(ss) in ag.inverse_xor3:
                    print(f'found, an FA @{var(i)}', '+'.join(map(lstr, ss)))
                    assert len(ag.inverse_xor3[str(ss)]) ==1 
                    x = ag.inverse_xor3[str(ss)][0]
                    fix = [i for i in node]
                    ag.HAx[var(i)] .append(AGate_FA(node,[i, x], []))
                    ag.HAx[var(x.outputx[0])] .append(AGate_FA(node,[i, x], []))
                    pass
                pass
            pass
        
        pass
    pass

class AGate_HA(AGate):
    shape = 'invtriangle'
    name = 'HA'
    edge_label = ['c','s']
    def get_edge_label(self, i):
        return self.edge_label[ var(i) == var(self.outputx[0])]
    @staticmethod
    def identify(ag):
        reverse_xor2 = defaultdict(list)
        xor2x = filter(ag.is_xor, ag.acc.topox)
        for i in map(ag.get_xor, xor2x):
            reverse_xor2[str(natsorted(pure(i)))].append(i)
            print('xor2 insert, ', natsorted(pure(i)), '->', var(i.outputx[0]))
            pass
        for i in ag.acc.topox:
            if ag.acc.fanout_cnt[var(i)] <=1: continue
            fin = ag.aiger.get_fanins(i)
            key = natsorted(pure(fin))
            print('try ha', key)
            if str(key) in reverse_xor2:
                
                f = reverse_xor2[str(key)]
                print(f'find half adder: {var(i)}, {var(f[0].outputx[0])} = HA({key})')
                assert len(f) == 1
                new_gate = AGate_HA(fin, [ f[0].outputx[0],i], [])
                ag.HAx[var(i)].append(new_gate)
                ag.HAx[var(f[0].outputx[0])].append(new_gate)
                pass

            pass
        pass
    pass

def Identify_chain(acc, i, gate_type):
    g = acc.gatex[var(i)][0]
    f = pure(g.outputx[0])
    assert var(f) == var(i)
    assert isinstance(acc.gatex[var(f)][0], gate_type)
    assert acc.gatex[var(f)][0] == g
    
    lx = list(_Identify_chain_r(acc, pure(f), gate_type))
    
    faninx = list(filter(lambda i: i[1] == 0, lx))
    internalx = list(filter(lambda i: i[1] == 1, lx))
    faninx , _  = zip(*faninx)
    internalx , _ =  zip(*internalx)
    if len(lx) > 3: 
        print(f"Found chain {gate_type.__name__}:", f"{var(f)} = %s" % (" $ ".join(map(lstr,faninx))))
        print(internalx)
        pass
    return g, faninx, internalx

    
def _Identify_chain_r(acc, g, gate_type):
    if not acc.is_gate(g, gate_type): 
        yield g, 0
        return 

    for input in acc.get_gate(g, gate_type):
        for j in _Identify_chain_r(acc, input, gate_type):
            yield j
            pass
        pass
    yield g, 1
    
    pass
        
