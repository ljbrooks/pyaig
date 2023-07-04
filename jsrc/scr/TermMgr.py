

class TermList(dict):
    pass

class UniqueTable(dict):
    def __init__(self):

        pass
    
    pass

class TermMgr(list):
    builder = None
    tmgr = None
    UID = 0
    tlist = TermList()
    
    unique = UniqueTable()
    
    @staticmethod
    def put(key, val):
        assert not key in TermMgr.unique
        TermMgr.unique[key] = val
        return val
    
    @staticmethod
    def get(key):
        return TermMgr.unique[key]

    def append(self, a):
        list.append(self, a)
        pass
    pass

if TermMgr.tmgr is None:
    TermMgr.tmgr = TermMgr()

    pass
