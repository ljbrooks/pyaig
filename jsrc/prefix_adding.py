from adder_util import *
from functools import *
from strlib import *
import operator
from operator import *
from jtag3 import jtag
from fplib import *


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


def pprefix_add_plain(x, y, cin):
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
    pgx = fmap(lambda i: PG(*i), zip(ps, gs)) + [pg0]

    # this is to compute the prefix
    # ppx = accumulate_r1(rplus)(pgx)
    # plain
    ppx = compute_prefix(pgx[:-1], pgx[-1])
    # Sklansky
    ppx2 = compute_prefix_r(pgx)
    print(ppx)
    print(ppx2)
    assert ppx == ppx2
    # assert False

    ppx_brunt = compute_prefix_brent_kung(pgx)
    assert ppx_brunt == ppx

    ppx_ks = compute_prefix_Kogge_Stone(pgx)
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
def compute_prefix_brent_kung(pgx):
    ff = lambda P1, P0: P1.__rplus__(P0)

    # need to reverse the pgx
    pgx = list(reversed(pgx))
    result = pgx
    result[0] = pgx[0]

    for i in range(1, len(pgx)):
        px = [result[j] for j in chop_for_prefix(i)]

        # left reduce is to create the correct structure
        result[i] = left_reduce1(ff)(px)
        pass
    return list(reversed(result))


# Brent Kung / using level
def compute_prefix_brent_kung_v2(pgx, level, instep=4):
    # level starts with 0

    step = 2 ** level
    rx = freversed(pgx)

    # the step is used for han-carlson algorithm
    for u,v in list(zip(rx[step-1::step*2], rx[2*step-1::step*2])):
        u.rplus(v)
        pass
    
    return freversed(rx)

def han_carlson_mid_layer(pgx, step):
    
    rx = zip(pgx[::step], pgx[step::step])
    fmap(lambda i: i[0].rplus(i[1]), fff, rx)
    
    pass



# Kogge–Stone
def compute_prefix_Kogge_Stone(pgx):
    ret = [i for i in pgx]
    i = 1
    while i < len(pgx):
        fmap(lambda u: u[0].rplus(u[1]), zip(pgx[:-i], pgx[i:]))
        i *= 2  # cool
        pass
    return ret

# Han Carlson 1
def compute_prefix_han_carlson1(pgx):
    # first pass is brent-kung

    # Second pass is kogge-stone


    # third is brent-kung again
    
    pass


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
