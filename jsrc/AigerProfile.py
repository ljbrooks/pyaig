from AigerCoiCluster import *
from AGuessGate import *
import pyaig, sys
from  natsort import *
import re
from collections import Counter
import pyparsing as pp
from tabulate import *
class AigerProfile:
    def __init__(self, aiger):
        self.aiger = aiger
        self.ag = AGuessGate(aiger)
        self.acc = self.ag.acc
        self.print_inputs()
        self.print_pp()
        self.print_maj3()
        self.profile_first_level_maj()
        pass

    def get_id_name(self, i):
        if i in self.aiger._id_to_name:
            return self.aiger._id_to_name[i].decode('utf-8')
        return None

    def print_inputs(self):
        for i in self.aiger.get_pis():
            name =  self.get_id_name(i)
            print (name)
            pass
        pass
    def print_pp(self):
        for i  in filter(lambda i: i, self.ag.ppx):
            f = i.outputx[0]
            ix = list(map(self.get_id_name, i))
            print (f'{var(f)} = {ix[0]} \\cdot {ix[1]}')
            pass
        pass
    def ssymbol(self,i):
        return ssign(i) + str(self.get_id_name(i))
    
    def get_pp_x_y(self, i):
        a,b = i[0], i[1]
        x = int(self.get_id_name(a).split('[')[1][:-1])
        y = int(self.get_id_name(b).split('[')[1][:-1])
        if self.get_id_name(a).split('[') == 'IN2':
            x.y = y,x
            pass
        return x,y
        
    def get_pp(self, i):
        print(i)
        pp = self.ag.ppx[var(i)]
        print('pp', pp)
        ix = list(map(self.get_id_name, pp))
        return f'{var(i)} = {ix[0]} \\cdot {ix[1]}'
        
    def get_gate_fanins(self, i):
        if self.ag.is_gate(i, AGate_AND):
            return self.ag.get_gate(i, AGate_AND)
        else :
            return self.aiger.get_fanins(i)
        pass
    def profile_first_level_maj(self):
        
        majx = list(filter(lambda i: self.ag.is_gate(i, AGate_Majority3) and self.acc.levelx[var(i)]<=4, self.acc.topox))
        maj_gatex = list(map(lambda i: self.ag.get_gate(i,  AGate_Majority3), majx))
        
        ppx = sum(map(lambda i: list(map(pure, i)),  maj_gatex), [])
        assert len(ppx) > 1
        for i in ppx:
            j = self.get_gate_fanins(i)
            #print('yay', i)
            #print(f'maj: {var(i)}: %s' % (','.join(map(lambda v: self.get_pp_x_y, j))))
            print(self.get_pp_x_y, j)
            pass
        
        xy = list(map(lambda i: self.get_pp_x_y(self.get_gate_fanins(i)), ppx))
        x_max = max(list(zip(*xy))[0])+1
        y_max = max(list(zip(*xy))[1])+1
        m = [[0]*y_max for i in range(x_max)]
        
        for x,y in xy: m[x][y]+=1
        
        print(tabulate(m))
        

        ix = sum(map(lambda i: self.get_gate_fanins(i), ppx) ,[])
        nx = map(self.get_id_name, ix)
        print(tabulate(natsorted(Counter(nx).items())))
        ix = set(ix)
        
        print('\n'.join(map(self.get_id_name, ix)))
        pass
            
                         
    def print_maj3(self):
        for  i in filter(lambda i: self.ag.is_gate(i, AGate_Majority3) and self.acc.levelx[var(i)]==4,
                         self.acc.topox):
            g = self.ag.get_gate(i, AGate_Majority3)
            print(g)

            print(f'{var(i)} is maj(%s)' % (','.join(map(lstr,g))), 'level is', self.acc.levelx[var(i)])
            print(f'{var(i)} is maj(%s)' % (','.join(map(self.ssymbol,g))), 'level is', self.acc.levelx[var(i)])
            print(f'{var(i)} is maj(%s)' % (','.join(map(self.get_pp, g))), 'level is', self.acc.levelx[var(i)])
            pass
            
        pass
    pass

if __name__ == '__main__':
    from filex import f
    #fx = '/home/long/uu/genmul/8_8_U_SP_WT_KS_GenMul.v.aig'.split()
    if len(sys.argv)>1: f = sys.argv[1]
    a = pyaig.aig_io.read_aiger(f)
    ap = AigerProfile(a)
    
    pass
