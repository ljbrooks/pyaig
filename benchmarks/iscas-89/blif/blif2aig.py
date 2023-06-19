

import os, glob
ax = glob.glob('*.blif')

cmd = 'abc -c "read_blif %s; strash; write %s.aig;" '

for i in ax:
    e = cmd % (i, i[:-5])
    print(e)
    os.system(e)

    pass
