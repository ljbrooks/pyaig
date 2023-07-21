import subprocess as sp
import sys, os
from pathlib import Path
import datetime


cmd = " ".join(sys.argv)

pwd = os.getcwd()

now = str(datetime.datetime.now())
log = Path(os.environ["HOME"]) / "hist.log"
log2 = Path(os.environ["HOME"]) / ".hist.log"

logx = [log, log2, "hist.log"]

host = None
if "HOSTNAME" in os.environ:
    host = os.environ["HOSTNAME"]
if not host:
    host = sp.run("hostname", stdout=sp.PIPE).stdout.decode("utf-8").strip()
    pass
if not host:
    host = None

host = str(host)


class Hist:
    Done = False

    def __init__():
        pass

    pass


if not Hist.Done:
    for log in logx:
        os.system(f"touch {log}")
        fx = open(log, "r").read().strip().splitlines()
        fx = list(filter(lambda i: i.startswith(host), fx))
        n = len(fx)

        s = f"""{host} {n} {now} pwd : {pwd} cmd : {cmd}
"""
        open(log, "a").write(s)
        pass
    Hist.Done = True
    pass
