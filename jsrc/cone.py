import history
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent/'..'))

import pyaig


def cone(aig):
    
    a = pyaig.aig_io.read_aiger(aig)
    
    if len(list(a.get_pos()))> 1:
        nx = range(len(list(a.get_pos())))
        for i in nx:
            ox = [list(a.get_pos())[i]]
            #ox = [j for i,j in enumerate(a.get_pos()) if i in nx]
            
            b = a.clean([i])
            fname ='%s_out_%s.aig' % (aig, i)
            pyaig.aig_io.write_aiger(b,fname)
            print('Gen', fname)
            pass
        pass
    pass

if __name__ == '__main__':
    
    aig, nx = sys.argv[1], list(map(int, sys.argv[2:]))
    cone(aig)
