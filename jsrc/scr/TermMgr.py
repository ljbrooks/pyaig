

class TermList(list):
    pass

class UniqueTable:
    def __init__(self):
        self.d = {}
        pass
    
    @staticmethod
    def put(key, val):
        assert not key in TermMgr.unique
        TermMgr.unique.d[key] = val
        return val
    @staticmethod
    def get(key):
        return TermMgr.unique.d[key]

    pass

class TermMgr(UniqueTable, list):
    builder = None
    tmgr = None
    UID = 0
    tlist = TermList()
    
    unique = UniqueTable()
    
    def append(self, a):
        list.append(self, a)
        pass
    pass

if TermMgr.tmgr is None:
    TermMgr.tmgr = TermMgr()
    pass
