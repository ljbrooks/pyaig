from functools import *
from fplib import *


def g(x, y):
    return x & y


def p(x, y):
    return x ^ y


def t(x, y):
    return g(x, y) | p(x, y)


def g(x):
    return x[0] & x[1]


def p(x):
    return x[0] ^ x[1]


def t(x):
    return g(x) | p(x)


def a(x, y):
    return ~g(x, y)


def maj(a, b, c):
    return (a & b) | (a & c) | (b & c)


def s(a, b, c):
    return a ^ b ^ c


def to_bits(n):
    if n <= 1:
        yield n
    else:
        for i in to_bits(n // 2):
            yield i
            pass
        yield n % 2
        pass
    pass


def int2bits(n):
    return list(to_bits(n))


def bits2uint(bx):
    print(bx)
    a = reduce(lambda a, b: 2 * a + b, bx, 0)  # this is foldl
    # b = foldr(lambda a,b: 2a+b, bx)
    # print(a,b)
    # assert a == b
    b = left_reduce(lambda a, b: 2 * a + b, 0)(bx)

    assert a == b
    return a
