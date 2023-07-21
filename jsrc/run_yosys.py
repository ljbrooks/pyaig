from pathlib import Path
import sys
import os
import subprocess
from pathlib import Path
import sys
from cone import cone

sys.path.append(str(Path(__file__).parent / ".."))
import history

cmd = "find . -name \\*.v"
cmd2 = "find . -name \\*.sv"


def run_cmd(cmd):
    a = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    ax = a.stdout.decode("utf-8")

    return ax


ax = run_cmd(cmd).split() + run_cmd(cmd2).split()
# print('\n'.join(ax))
for i in ax:
    i = Path(i).name
    print(i)
    target_dir = "test/%s" % i[: i.rfind(".")]
    print(target_dir)
    os.system("mkdir -p %s" % target_dir)

    os.system(f"cp {i} {target_dir} ")
    pwd = os.getcwd()
    os.chdir(target_dir)
    e = (
        'yosys -p "read_verilog -sv %s ; hierarchy -auto-top ; flatten ; aigmap; write_aiger -symbols %s.aig"'
        % (i, i)
    )
    print(e)
    os.system(e)
    fname = "%s/%s.aig" % (target_dir, i)
    os.chdir(pwd)

    if os.path.exists(fname):
        cone(fname)
        pass

    pass


def sort_them_by_size():
    cmd = "ls -lhS *.aig"

    ax = run_cmd(cmd).splitlines()
    ax = [i.split()[-1] for i in ax]
    ax = list(reversed(ax))
    print("\n".join(ax))
    for i, j in enumerate(ax):
        cmd = f"ln -sf ../{j} links/pa_{str(i).zfill(2)}.aig"
        print(cmd)
        os.system(cmd)
    pass


# sort_them_by_size()
