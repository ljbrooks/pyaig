def var(i) : return i//2
def lstr(i): return '%s%s'% ('+-'[sign(i)],var(i))
def sign(lit): return (lit &0x1) == 1
def ssign(lit): return '+-'[int(sign(lit))]
def inv(lit) : 
    if isinstance(lit, int):
        return lit ^ 0x1
    assert isinstance(lit, list)
    return list(map(inv, lit))

def pure(lit):
    i = lit
    if isinstance(lit, int):
        return i ^ (i&0x1)
    assert isinstance(lit, list)
    return list(map(pure, lit))

def edge_style(i):
    return 'dotted' if sign(i) else ""
def edge_color(i):
    return 'blue' if sign(i) else ""
def dprint(*args): pass

def inv_one(litx):
    bx = list(map(sign, litx))
    cnt = sum(bx)               # number of True
    if cnt ==2 or cnt == 0:
        x = bx.index(False)
        litx[x] = inv(litx[x])
        pass
    else :
        x = bx.index(True)
        litx[x] = inv(litx[x])
        pass
    return litx
def make_lit(v, signbit):
    return (v<<1) ^ signbit
