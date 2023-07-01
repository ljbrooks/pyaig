import history

import sys
sys.path.append('..')

import pyaig
aig, nx = sys.argv[1], list(map(int, sys.argv[2:]))


print(aig, nx)

a = pyaig.aig_io.read_aiger(aig)

ox = [j for i,j in enumerate(a.get_pos()) if i in nx]

b = a.clean(nx)
fname ='%s_out_%s.aig' % (aig, '_'.join(map(str,nx)))
pyaig.aig_io.write_aiger(b,fname)
print('Gen', fname)

