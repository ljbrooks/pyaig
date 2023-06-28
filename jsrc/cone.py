import pyaig

import sys

aig, nx = sys.argv[1], list(map(int, sys.argv[2:]))


print(aig, nx)

a = pyaig.aig_io.read_aiger(aig)

ox = [j for i,j in enumerate(a.get_pos()) if i in nx]

b = a.clean(nx)

pyaig.aig_io.write_aiger(b,'t.aig')
print('gen t.aig')
