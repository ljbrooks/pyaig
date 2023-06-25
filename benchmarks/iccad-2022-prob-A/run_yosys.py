
import sys
import os
import subprocess

cmd = 'find . -name *.v'

def run_cmd(cmd):
    a = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    ax = a.stdout.decode('utf-8')
    return ax
#print('\n'.join(ax))

ax = run_cmd(cmd).split()
for i in ax:
    e = 'yosys -p "read_verilog -sv %s ; hierarchy -auto-top ; flatten ; aigmap; write_aiger %s.aig"' % (i,i)
    print(e)
    #os.system(e)
    pass


def sort_them_by_size():
    cmd ='ls -lhS */*/*.aig'
    
    ax  = run_cmd(cmd).splitlines()
    ax = [i.split()[-1] for i in ax]
    ax = list(reversed(ax))
    print('\n'.join(ax))
    for i,j in enumerate(ax):
        cmd = f"ln -sf ../{j} links/pa_{str(i).zfill(2)}.aig"
        print(cmd)
        os.system(cmd)
    pass

sort_them_by_size()
