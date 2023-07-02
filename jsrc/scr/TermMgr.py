class TermMgr(list):
    tmgr = None
    UID = 0
    pass

if TermMgr.tmgr is None:
    TermMgr.tmgr = TermMgr()
