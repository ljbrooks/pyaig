
import sys, os
from pathlib import Path
import datetime


cmd = ' '.join(sys.argv)

pwd = os.getcwd()

now = str(datetime.datetime.now())
log = Path(os.environ['HOME'])/'hist.log'
log2 = Path(os.environ['HOME'])/'.hist.log'

logx = [log, log2, 'hist.log']


host = os.environ['HOST']
class Hist:
    Done = False
    def __init__():
        pass
    pass

if not Hist.Done :
    for log in logx:
        os.system(f'touch {log}')
        fx = open(log,'r').read().strip().splitlines()
        n = len(fx)
        s = f'''{n} {host} {now} pwd : {pwd} cmd : {cmd}
'''
        open(log,'a').write(s)
        pass
    Hist.Done = True
    pass
    

