
import sys
import os
import subprocess

cmd = 'find . -name *.v'

a = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
ax = a.stdout.decode('utf-8').split()
#print('\n'.join(ax))

for i in ax:
    e = 'yosys -p "read_verilog -sv %s ; hierarchy -auto-top ; flatten ; aigmap; write_aiger %s.aig"' % (i,i)
    print(e)
    os.system(e)
    pass
