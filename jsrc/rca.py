from jtag3 import jtag
from fplib import *

from functools import *
from strlib import *
import operator
from operator import *
from prefix_adding import *
from adder_util import *

def rca(x,y):
    # ripple adder is a combinator
    
    if g((x[0], y[0])) : x , y = [0] + x , [0]+y # keep the carry bits

    #fa = lambda a,b, cin: ( maj(a,b,cin), s(a,b,cin) )
    
    fx = lambda x,y: (maj(x[0], x[1], y[0]), s(x[0], x[1], y[0]) )
    f = accumulate_r(lambda a, b: fx (a,b), (0,0))(zip(x,y))[:-1]
    print(f)
    return [i[1] for i in f]

def cla(x,y, cin=0):
    # carry look ahead
    ps = fmap(p, zip(x,y))
    gs = fmap(lambda i: g(i),zip(x,y))

    # f( (p,g), cin) = g + p\cdot cin
    
    # c_next = g + p \cdot cin
    # right_reduce
    f = lambda pg, c: pg[1] | (c & pg[0])
    cx = accumulate_r(f, cin)(zip(ps,gs))
 
    jtag('x,y', [str(x),str(y)])
    jtag('carry[n:1]', str(cx))

    jtag('ps', str(ps))
    jtag('gs', str(gs))
    r = fmap(lambda i: i[0] ^ i[1], zip([0] + ps,cx))

    jtag('results', str((r, bits2uint(r), bits2uint(x), bits2uint(y))))
    
    return r

def cla2(x,y,cin=0):
    
    ps = fmap(lambda i:p(i), zip(x,y))
    gs = fmap(lambda i: g(i),zip(x,y))

    # f( (p,g), cin) = g + p\cdot cin
    #f = lambda a, b: a[1] | (b & a[0])
    f = lambda pg, c: pg[1] | (c & pg[0])

    jtag('tails', str(tails(zip(ps,gs))))
    cx = fmap(right_reduce(f, 0), tails(zip(ps,gs)))
    
    jtag('cla2-carry', str(cx))
    r = fmap(lambda i: i[0] ^ i[1], zip([0] + ps,cx+[cin]))

    jtag('result', str((r, bits2uint(r), bits2uint(x), bits2uint(y))))
    jtag('PASS',  str(bits2uint(r) == bits2uint(x) + bits2uint(y)))
    pass

def cla3(x,y,cin=0):
    
    ps = fmap(lambda i:p(i), zip(x,y))
    gs = fmap(lambda i: g(i),zip(x,y))

    # f( (p,g), cin) = g + p\cdot cin

    #f = lambda a, b: a[1] | (b & a[0])
    f = lambda pg, c: pg[1] | (c & pg[0])

    jtag('tails', str(tails(zip(ps,gs))))
    cx = fmap(right_reduce(f, cin), tails(zip(ps,gs)))
    
    jtag('cla2-carry', str(cx))
    r = fmap(lambda i: i[0] ^ i[1], zip([0] + ps,cx+[cin]))

    jtag('result', str((r, bits2uint(r), bits2uint(x), bits2uint(y))))
    jtag('PASS',  str(bits2uint(r) == bits2uint(x) + bits2uint(y)))
    pass

def ling_adder_with_t(x,y, cin=0):
    ts = fmap(lambda i:t(i), zip(x,y))
    gs = fmap(lambda i: g(i),zip(x,y))
    ps = fmap(lambda i: p(i),zip(x,y))
    # f( (p,g), cin) = g + p\cdot cin
    f = lambda a, b: a[1] | (b & a[0])
    # need to compute he
    '''
    h0 = cin
    h1 = c1 + cin
    h_next = g + h \cdot t_prev
    '''
    f = lambda gt, c: gt[0] | (gt[1] & c)
    
    cx = fmap(right_reduce(f, cin), tails(zzip(gs,ts)))

    jtag('ling-adder-carry', str(cx))
    r = fmap(lambda i: i[0] ^ i[1], zip([0] + ps,cx+[cin]))

    jtag('result', str((r, bits2uint(r), bits2uint(x), bits2uint(y))))
    jtag('PASS',  str(bits2uint(r) == bits2uint(x) + bits2uint(y)))
    assert bits2uint(r) == bits2uint(x) + bits2uint(y)
    return r

def ling_adder(x,y,cin=0):
    ts = [0] + fmap(lambda i:t(i), zip(x,y))
    gs = [0] + fmap(lambda i: g(i),zip(x,y))
    ps = [0] + fmap(lambda i: p(i),zip(x,y))

    c1 = gs[-1] | (ps[-1] & cin)
    
    h1 = c1 | cin

    h_fn = lambda i, h: gs[i+1]  | (h & ts[i+2])
    
    hs = accumulate_r(h_fn, h1)(range(len(gs)-2)) # right-reduce with tails

    assert len(hs) == len(gs) -1
    #assert False
    cx = fmap(lambda i:hs[i] & ts[i+1], range(len(gs)-1)) 
    
    cx += [cin]
    assert len(cx) == len(gs)
    
    jtag('ling-adder (hs)', str(hs))
    jtag('ling-adder cx', str(cx))

    #return 
    r = fmap(lambda i: i[0] ^ i[1], zip(ps,cx+[cin]))

    jtag('result', str((r, bits2uint(r), bits2uint(x), bits2uint(y))))
    jtag('PASS',  str(bits2uint(r) == bits2uint(x) + bits2uint(y)))
    assert bits2uint(r) == bits2uint(x) + bits2uint(y)
    
    return r


if __name__ == '__main__':
    
    for i in range(257):
        x = int2bits(i)
        y = bits2uint(x)
        assert y == i
        pass
    print(x)
    k = accumulate_l1(operator.__add__)( x)

    print(k)
    print(list(inits(x)))

    print(right_reduce(operator.__xor__, 1)(x))

    print(accumulate_l(operator.__add__, 0)(x))
    print(accumulate_r(operator.__add__, 0)(x))
    print(accumulate_r1(operator.__add__)(x))
    print(list(tails(x)))
    print(rca(x,x))
    u = rca(x,x)
    jtag('u',str(u))
    assert bits2uint(u) == bits2uint(x)*2
    y =  int2bits(272)
    assert len(x) == len(y)
    print(x,y)
    ps = list(map(lambda i: p(i), zip(x,y)))
    print(list(ps))
    gs = list(map(lambda i: g(i), zip(x,y)))
    print(list(gs))
    print(inits(ps))
    s = list(map(right_reduce(operator.__and__, 1),inits(ps)))
    print(s)
    cla(x,y)
    print(bits2uint(x) + bits2uint(y))
    cla2(x,y)
    jtag('x', str(x))
    jtag('tails', str(tails(x)))
    jtag('inits', str(inits(x)))
    u = ling_adder_with_t(x,y)
    jtag('ling_with_t', str(u))
    u = ling_adder(x,y)
    pprefix_add_plain(x,y,0)
