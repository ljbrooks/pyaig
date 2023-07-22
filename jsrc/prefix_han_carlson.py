from adder_util import *
from functools import *
from strlib import *
import operator
from operator import *
from jtag3 import jtag
from fplib import *


# Brent Kung / using level
def compute_prefix_brent_kung_v2(pgx, level, instep=4):
    # level starts with 0

    step = 2 ** level
    rx = freversed(pgx)

    # the step is used for han-carlson algorithm
    for u, v in list(zip(rx[step - 1 :: step * 2], rx[2 * step - 1 :: step * 2])):
        u.rplus(v)
        pass

    return freversed(rx)


def han_carlson_mid_layer(pgx, step):

    rx = zip(pgx[::step], pgx[step::step])
    fmap(lambda i: i[0].rplus(i[1]), fff, rx)

    pass


# Han Carlson 1
def compute_prefix_han_carlson1(pgx):
    # first pass is brent-kung
    compute_prefix_brent_kung_v2(pgx, 0)
    # Second pass is kogge-stone

    # third is brent-kung again
    compute_prefix_brent_kung_v2(pgx, 0)
    pass
