import sys
import os

USER = os.environ["USER"] if "USER" in os.environ else "UnkUser"
LJ_DEBUG = "LJ_DEBUG"
is_debug = LJ_DEBUG in os.environ or USER == "jlong" or USER == "long"
dmsg = lambda x: "[DEBUG] %s " % x if is_debug_msg else x


class jtagCfg:
    PREFIX = None

    pass


def SetPrefix(p):
    jtagCfg.PREFIX = p


def TagIt(tag_):
    return tag_ if jtagCfg.PREFIX is None else "%s %s" % (jtagCfg.PREFIX, tag_)


def jtag(tag_, msg_, bs=-1, debug_=False, noskip=False):
    global is_debug_msg
    is_debug_msg = debug_
    ret = []
    if tag_ != None:
        if noskip:
            print
            pass

        ret.append(
            "%-60s%20s" % (dmsg(TagIt(tag_)) + ":", "%s......" % (getCallser(bs)))
        )
        print(ret[-1])
        ret.append(dmsg("=" * len(tag_)))
        print(dmsg("=" * len(tag_)))
        pass
    if msg_ == None:
        ax = []
        pass
    elif isinstance(msg_, str):
        ax = msg_.splitlines()
        pass
    elif isinstance(msg_, int):
        ax = [str(msg_)]
    else:
        if not isinstance(msg_, list):
            print("Unexpected type", type(msg_))
            pass
        assert isinstance(msg_, list)
        ax = []
        for i in msg_:
            ax = ax + i.splitlines()
            pass
        if not len(ax):
            ax = ["None"]
        pass
    if len(ax):
        print("\n".join([dmsg("    " + i) for i in ax]))
        ret.append("\n".join([dmsg("    " + i) for i in ax]))
        if tag_:
            print
            ret.append("")
        pass
    is_debug_msg = False
    sys.stdout.flush()
    return "\n".join(ret)
    pass


def jtag_debug(tag_, msg_):
    global is_debug
    jtag(tag_, msg_, is_debug)

    pass


def jassert(expr, msg_=None):
    if not expr:
        print("--------------------------------------------------")
        jtag("Internal Error", "Contact jiang_long@apple.com")
        print("--------------------------------------------------")
        pass
    assert expr
    pass


import inspect


def hello():
    previous_frame = inspect.currentframe().f_back
    (filename, line_number, function_name, lines, index) = inspect.getframeinfo(
        previous_frame
    )
    return (filename, line_number, function_name, lines, index)


import inspect


def getCallser(backframeNum):
    if "SAG_DEBUG" not in os.environ:
        return ""
    assert backframeNum < 0
    bs = backframeNum
    cur = inspect.currentframe()
    previous_frame = cur.f_back
    assert bs < 0
    for i in range(0, abs(bs)):
        cur, previous_frame = previous_frame, previous_frame.f_back
        pass
    (filename, line_number, function_name, lines, index) = inspect.getframeinfo(
        previous_frame
    )
    cur_fname = inspect.getframeinfo(cur)[0]
    ret = "%s:%d:%s" % (os.path.basename(filename), line_number, function_name)
    # print(  "## calling %s:%s from "% (cur_fname, inspect.getframeinfo(cur)[2]) ,
    return ret


def hello(bs):
    cur = inspect.currentframe()
    previous_frame = cur.f_back
    assert bs < 0
    for i in range(0, abs(bs)):
        cur, previous_frame = previous_frame, previous_frame.f_back
        pass
    (filename, line_number, function_name, lines, index) = inspect.getframeinfo(
        previous_frame
    )
    cur_fname = inspect.getframeinfo(cur)[0]
    print(
        "## calling %s:%s from " % (cur_fname, inspect.getframeinfo(cur)[2]),
        "%s:%d:%s" % (filename, line_number, function_name),
    )
    pass  # return (filename, line_number, function_name, lines, index)


# hello(-1)


def jtag0(bs, tag_, msg_):
    hello(bs)
    jtag(tag_, msg_, noskip=False)
    pass


def jtag_debug(tag_, msg_):
    global is_debug
    jtag(tag_, msg_, is_debug)

    pass


def jvl_assert_exists(fname):
    if not os.path.exists(fname):
        msg_ = "File %s does not exist" % fname
        jtag0(-2, "Aseert Error", msg_)
        assert os.path.exists(fname)
        pass
    pass


def jvl_assert(expr, msg_=None):
    if not expr:
        print("--------------------------------------------------")
        jtag0(-2, "Error", msg_)
        print
        jtag("Internal Error", "Contact jiang_long@apple.com")
        print("--------------------------------------------------")
        pass
    assert expr
    pass
