def isort(lx):
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
