from scr.Term import *

def isort(lx):
    if isinstance(lx, TermListUnordered):
        return lx
    isort_r(lx, 1)
    return lx

def isort_r(lx, i):
    if i>= len(lx): return 
    sort_in_place(lx, i)
    isort_r(lx, i+1)
    pass

def sort_in_place(lx, i):
    if i==0: return
    
    if lx[i]< lx[i-1]:
        lx[i], lx[i-1] = lx[i-1], lx[i]
        sort_in_place(lx, i-1)
        pass
    pass

def merge(x,y):
    assert not isinstance(x, TermListUnordered)
    assert not isinstance(y, TermListUnordered)
    r = []
    self.clear()
    assert isinstance(x, TermList)
    
    y.append(x.inf)
    x.append(y.inf)
    i,j = 0, 0
    for _  in range(len(x) + len(y) -2):
        if x[i] <= y[j] : 
            r.append(x[i])
            i+=1
        else:
            r.append(y[j])
            j+=1
            pass
        pass
    x.pop()
    y.pop()
    return TermList(r)

