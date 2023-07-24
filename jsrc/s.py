from scr.Term import *
from scr.TermTopo  import *
from scr.TermDot  import *


pp64 = Atom("pp_4_4")   # n64 --
pp58 = Atom("pp_3_3")   # n58 --
pp46 = Atom("pp_2_2")   # n46 --
pp40 = Atom("pp_1_1")   # n40 --
pp30 = Atom("pp_0_0")   # n30 --
pp28 = Atom("pp_IN1[0]_carryin")   # n28 --
pp32 = Atom("pp_IN2[0]_carryin")   # n32 --
pp86 = Atom("pp_5_5")   # n86 --
i26 = Atom("i13")   ## IN2[5]
i27 = ~ i26    ## IN2[5]
i14 = Atom("i7")   ## IN1[5]
i15 = ~ i14    ## IN1[5]
i2 = Atom("i1")   ## carryin
i3 = ~ i2    ## carryin
i16 = Atom("i8")   ## IN2[0]
i17 = ~ i16    ## IN2[0]
i4 = Atom("i2")   ## IN1[0]
i5 = ~ i4    ## IN1[0]
i18 = Atom("i9")   ## IN2[1]
i19 = ~ i18    ## IN2[1]
i6 = Atom("i3")   ## IN1[1]
i7 = ~ i6    ## IN1[1]
i20 = Atom("i10")   ## IN2[2]
i21 = ~ i20    ## IN2[2]
i8 = Atom("i4")   ## IN1[2]
i9 = ~ i8    ## IN1[2]
i22 = Atom("i11")   ## IN2[3]
i23 = ~ i22    ## IN2[3]
i10 = Atom("i5")   ## IN1[3]
i11 = ~ i10    ## IN1[3]
i24 = Atom("i12")   ## IN2[4]
i25 = ~ i24    ## IN2[4]
i12 = Atom("i6")   ## IN1[4]
i13 = ~ i12    ## IN1[4]
xs66 = scr.s(i12,i24, nid="xs66")
xs67 = scr.s(i13,i25, nid="xs67")
xs66 = scr.s(i12,i24, nid="xs66")
xs67 = scr.s(i13,i25, nid="xs67")
xc68 = scr.m2(xs66,pp58, nid="m268")
xc69 = ~ scr.m2(xs66,pp58, nid="m269")
xc70 = scr.m2(xc69,~pp64, nid="m270")
xc71 = ~ scr.m2(xc69,~pp64, nid="m271")
xs48 = scr.s(i8,i20, nid="xs48")
xs49 = scr.s(i9,i21, nid="xs49")
xs48 = scr.s(i8,i20, nid="xs48")
xs49 = scr.s(i9,i21, nid="xs49")
xc50 = scr.m2(xs48,pp40, nid="m250")
xc51 = ~ scr.m2(xs48,pp40, nid="m251")
xc52 = scr.m2(xc51,~pp46, nid="m252")
xc53 = ~ scr.m2(xc51,~pp46, nid="m253")
xs60 = scr.s(i10,i22, nid="xs60")
xs61 = scr.s(i11,i23, nid="xs61")
xs60 = scr.s(i10,i22, nid="xs60")
xs61 = scr.s(i11,i23, nid="xs61")
xc72 = scr.m2(xs66,xs60, nid="m272")
xc73 = ~ scr.m2(xs66,xs60, nid="m273")
xc74 = scr.m2(xc72,xc53, nid="m274")
xc75 = ~ scr.m2(xc72,xc53, nid="m275")
xc76 = scr.m2(xc75,xc70, nid="m276")
xc77 = ~ scr.m2(xc75,xc70, nid="m277")
hc36 = scr.c(i17,i3,i5, nid="hc36")
hc37 = scr.c(i16,i2,i4, nid="hc37")
xs42 = scr.s(i6,i18, nid="xs42")
xs43 = scr.s(i7,i19, nid="xs43")
xs42 = scr.s(i6,i18, nid="xs42")
xs43 = scr.s(i7,i19, nid="xs43")
xc54 = scr.m2(xs48,xs42, nid="m254")
xc55 = ~ scr.m2(xs48,xs42, nid="m255")
xc78 = scr.m2(xc72,xc54, nid="m278")
xc79 = ~ scr.m2(xc72,xc54, nid="m279")
xc80 = scr.m2(xc78,~hc36, nid="m280")
xc81 = ~ scr.m2(xc78,~hc36, nid="m281")
xc82 = scr.m2(xc81,xc76, nid="m282")
xc83 = ~ scr.m2(xc81,xc76, nid="m283")
xs88 = scr.s(i14,i26, nid="xs88")
xs89 = scr.s(i15,i27, nid="xs89")
xs88 = scr.s(i14,i26, nid="xs88")
xs89 = scr.s(i15,i27, nid="xs89")
xs94 = scr.s(xc82,~xs88, nid="xs94")
xs95 = scr.s(xc83,xs88, nid="xs95")
xs94 = scr.s(xc82,~xs88, nid="xs94")
xs95 = scr.s(xc83,xs88, nid="xs95")
pox = [xs94]
