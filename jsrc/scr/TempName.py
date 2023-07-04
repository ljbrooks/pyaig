

class TempName:
    def __init__(self, prefix='tmp'):
        self.tid = 0
        pass
    
    def gen(self):
        r = f'{self.prefix}_{self.tid}' 
        self.tid +=1
        return r
    pass
