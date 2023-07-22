from adder_util import *
from functools import *
from strlib import *
import operator
from operator import *
from jtag3 import jtag
from fplib import *
from prefix_han_carlson import *

class PG:
    def __init__(self, p, g):
        self.p, self.g = p, g
        pass

    def __rplus__(self, x):
        p = self.p ^ x.p
        g = self.g | (self.p & x.g)
        return PG(p, g)

    def rplus(self, x):
        p = self.p ^ x.p
        g = self.g | (self.p & x.g)
        self.p, self.g = p, g
        return self

    def __eq__(self, a):
        return self.p, self.g == a.p, a.g

    def __str__(self):
        return f"({self.p},{self.g})"

    def __repr__(self):
        return str(self)

    pass

def level_xy(x,y):
    if len(x) > len(y): x,y = y,x
    x = [0] * (len(y)-len(x)) + x
    return x,y
def pprefix_add_plain(x, y, cin):
    x,y = level_xy(x,y)
        
    ts = fmap(lambda i: t(i), zip(x, y))
    gs = fmap(lambda i: g(i), zip(x, y))
    ps = fmap(lambda i: p(i), zip(x, y))
    ppx = pprefix(x, y, cin)

    # carry
    cx = fmap(lambda i: i.g, ppx) + [cin]
    print("pprefix_add_plain cx", str(cx))

    # result
    r = sx = fmap(lambda a: a[0] ^ a[1], zip(cx, [0] + ps))

    print("pprefix_add_plain", str(r))
    jtag("result", str((r, bits2uint(r), bits2uint(x), bits2uint(y))))
    jtag("PASS", str(bits2uint(r) == bits2uint(x) + bits2uint(y)))
    
    assert bits2uint(r) == bits2uint(x) + bits2uint(y)

    return r


def pprefix(x, y, cin):

    ts = fmap(lambda i: t(i), zip(x, y))
    gs = fmap(lambda i: g(i), zip(x, y))
    ps = fmap(lambda i: p(i), zip(x, y))
    rplus = lambda P1, P0: P1.__rplus__(P0)

    # init the cin bit
    pg0 = PG(0, cin)
    # init the pgx list
    pgx = fmap(lambda i: PG(*i), zip(ps, gs)) + [PG(0, cin)]

    # this is to compute the prefix
    # ppx = accumulate_r1(rplus)(pgx)
    # plain
    ppx = compute_prefix(pgx[:-1], pgx[-1])
    # Sklansky
    pgx = fmap(lambda i: PG(*i), zip(ps, gs)) + [PG(0, cin)]
    ppx2 = compute_prefix_r(pgx)
    print(ppx)
    print(ppx2)
    assert ppx == ppx2
    # assert False
    
    pgx = fmap(lambda i: PG(*i), zip(ps, gs)) + [PG(0, cin)]
    ppx_brunt = compute_prefix_brent_kung_bug(pgx)
    assert ppx_brunt == ppx

    pgx = fmap(lambda i: PG(*i), zip(ps, gs)) + [PG(0, cin)]
    ppx_ks = compute_prefix_Kogge_Stone(pgx)

    pgx = fmap(lambda i: PG(*i), zip(ps, gs)) + [PG(0, cin)]
    pgx = list(reversed(pgx))
    pgx2 = brunt_r(pgx, 1)
    pgx2 = list(reversed(pgx2))
    print(pgx2)
    jtag('pgx2', str(pgx2))
    assert pgx2 == ppx_brunt
    assert ppx_brunt == ppx_ks

    return ppx


def compute_prefix(pgx, pg0):
    rplus = lambda P1, P0: P1.__rplus__(P0)
    ppx = accumulate_r(rplus, pg0)(pgx)
    return ppx


# Sklansky
def compute_prefix_r(pgx):
    if len(pgx) <= 1:
        return pgx

    mid = len(pgx) // 2
    a = compute_prefix_r(pgx[:mid])
    b = compute_prefix_r(pgx[mid:])

    ff = lambda P1, P0: P1.__rplus__(P0)

    # merge step
    a = fmap(lambda i: ff(i, b[0]), a)

    return a + b


# Brent Kung / using chop
def compute_prefix_brent_kung_bug(pgx):
    ff = lambda P1, P0: P1.__rplus__(P0)

    # need to reverse the pgx
    pgx = list(reversed(pgx))
    pgx2 = [i for i in pgx]
    result = pgx
    result[0] = pgx[0]

    for i in range(1, len(pgx)):
        print('chop', chop_for_prefix(i))
        px = [result[j] for j in chop_for_prefix(i)]

        # left reduce is to create the correct structure
        result[i] = left_reduce1(ff)(px)
        pass
    


    #assert pgx == pgx2
    return list(reversed(result))


def brunt_r(pgx, step):
    # step starts with 2
    #assert step >= 2
    if (step >= len(pgx)) :return  pgx
    N = len(pgx)

    rx = range(2*step-1, N, step)
    is_even = lambda i: i%2 == 0     

    even = [j for i,j in enumerate(rx) if is_even(i)]
    odd = [j for i,j in enumerate(rx) if not is_even(i)]
    
    for i in even:   pgx[i].rplus(pgx[i-step])

    brunt_r(pgx, step*2)

    for i in odd:  pgx[i].rplus(pgx[i-step])
    return pgx


# Kogge–Stone
def compute_prefix_Kogge_Stone(pgx):
    ret = [i for i in pgx]
    i = 1
    while i < len(pgx):
        fmap(lambda u: u[0].rplus(u[1]), zip(pgx[:-i], pgx[i:]))
        i *= 2  # cool
        pass
    return ret



def pprefix_lf(x, y, cin):
    # basically divide and conquer and compute the prefix

    pass


def chop(x):
    if x == 0:
        return
    r = (x ^ (x - 1)) & x
    x = x & (~r)
    for i in chop(x):
        yield i
    yield r
    pass


def chop_for_prefix(x):
    rx = list(chop(x))
    if len(rx) == 1:
        rx.append(x - 1)
        pass
    return rx


if __name__ == "__main__":
    for i in range(100):
        u = list(chop(i))
        # print(u)
        # print(sum(u)) bits2uint(u), i)
        assert sum(u) == i
        u = list(chop_for_prefix(i))
        print(i, u)
        pass
    pass
