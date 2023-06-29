
import sys, os
from pathlib import Path
import datetime


cmd = ' '.join(sys.argv)

pwd = os.getcwd()

now = str(datetime.datetime.now())
log = Path(os.environ['HOME'])/'hist.log'
log2 = Path(os.environ['HOME'])/'.hist.log'
class Hist:
    Done = False
    def __init__():
        pass
    pass

if not Hist.Done :
    s = f'''{now} pwd : {pwd} cmd : {cmd}
'''
    
    open(log,'a').write(s)
    open(log2,'a').write(s)
    Hist.Done = True
    pass
    

