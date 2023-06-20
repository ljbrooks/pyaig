

import pyaig
from dd.cudd import BDD
import networkx as nx
f = '../../benchmarks/arithmetic/adder.aig'

a = pyaig.aig_io.read_aiger(f)



bddx = [None] 
