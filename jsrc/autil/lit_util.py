def var(i) : return i//2
def lstr(i): return '%s%s'% ('+-'[sign(i)],var(i))
def sign(lit): return (lit &0x1) == 1
def ssign(lit): return '+-'[int(sign(lit))]
def inv(lit) : 
    if isinstance(lit, int):
        return lit ^ 0x1
    assert isinstance(lit, list)
    return list(map(inv, lit))
def pure(i): return i ^ (i&0x1)
def edge_style(i):
    return 'dotted' if sign(i) else ""
def edge_color(i):
    return 'blue' if sign(i) else ""
def dprint(*args): pass
