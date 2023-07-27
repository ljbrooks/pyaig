from scr.Term import *
from scr.TermTopo  import *
from scr.TermDot  import *


pp104 = Atom("pp_7_7")   # n104 --
pp98 = Atom("pp_6_6")   # n98 --
pp86 = Atom("pp_5_5")   # n86 --
pp80 = Atom("pp_4_4")   # n80 --
pp64 = Atom("pp_3_3")   # n64 --
pp58 = Atom("pp_2_2")   # n58 --
pp48 = Atom("pp_1_1")   # n48 --
pp38 = Atom("pp_0_0")   # n38 --
pp36 = Atom("pp_IN1[0]_carryin")   # n36 --
pp40 = Atom("pp_IN2[0]_carryin")   # n40 --
i2 = Atom("i1_carryin")   ## carryin
i3 = ~ i2    ## carryin
i20 = Atom("i10_IN2[0]")   ## IN2[0]
i21 = ~ i20    ## IN2[0]
i4 = Atom("i2_IN1[0]")   ## IN1[0]
i5 = ~ i4    ## IN1[0]
i22 = Atom("i11_IN2[1]")   ## IN2[1]
i23 = ~ i22    ## IN2[1]
i6 = Atom("i3_IN1[1]")   ## IN1[1]
i7 = ~ i6    ## IN1[1]
i24 = Atom("i12_IN2[2]")   ## IN2[2]
i25 = ~ i24    ## IN2[2]
i8 = Atom("i4_IN1[2]")   ## IN1[2]
i9 = ~ i8    ## IN1[2]
i26 = Atom("i13_IN2[3]")   ## IN2[3]
i27 = ~ i26    ## IN2[3]
i10 = Atom("i5_IN1[3]")   ## IN1[3]
i11 = ~ i10    ## IN1[3]
i28 = Atom("i14_IN2[4]")   ## IN2[4]
i29 = ~ i28    ## IN2[4]
i12 = Atom("i6_IN1[4]")   ## IN1[4]
i13 = ~ i12    ## IN1[4]
i30 = Atom("i15_IN2[5]")   ## IN2[5]
i31 = ~ i30    ## IN2[5]
i14 = Atom("i7_IN1[5]")   ## IN1[5]
i15 = ~ i14    ## IN1[5]
i32 = Atom("i16_IN2[6]")   ## IN2[6]
i33 = ~ i32    ## IN2[6]
i16 = Atom("i8_IN1[6]")   ## IN1[6]
i17 = ~ i16    ## IN1[6]
i34 = Atom("i17_IN2[7]")   ## IN2[7]
i35 = ~ i34    ## IN2[7]
i18 = Atom("i9_IN1[7]")   ## IN1[7]
i19 = ~ i18    ## IN1[7]
xs106 = scr.s(i18,i34, nid="xs106")
xs107 = scr.s(i19,i35, nid="xs107")
xs106 = scr.s(i18,i34, nid="xs106")
xs107 = scr.s(i19,i35, nid="xs107")
xc108 = scr.m2(xs106,pp98, nid="m2108")
xc109 = ~ scr.m2(xs106,pp98, nid="m2109")
xc110 = scr.m2(xc109,~pp104, nid="m2110")
xc111 = ~ scr.m2(xc109,~pp104, nid="m2111")
xs88 = scr.s(i14,i30, nid="xs88")
xs89 = scr.s(i15,i31, nid="xs89")
xs88 = scr.s(i14,i30, nid="xs88")
xs89 = scr.s(i15,i31, nid="xs89")
xc90 = scr.m2(xs88,pp80, nid="m290")
xc91 = ~ scr.m2(xs88,pp80, nid="m291")
xc92 = scr.m2(xc91,~pp86, nid="m292")
xc93 = ~ scr.m2(xc91,~pp86, nid="m293")
xs100 = scr.s(i16,i32, nid="xs100")
xs101 = scr.s(i17,i33, nid="xs101")
xs100 = scr.s(i16,i32, nid="xs100")
xs101 = scr.s(i17,i33, nid="xs101")
xc112 = scr.m2(xs106,xs100, nid="m2112")
xc113 = ~ scr.m2(xs106,xs100, nid="m2113")
xc114 = scr.m2(xc112,xc93, nid="m2114")
xc115 = ~ scr.m2(xc112,xc93, nid="m2115")
xc116 = scr.m2(xc115,xc110, nid="m2116")
xc117 = ~ scr.m2(xc115,xc110, nid="m2117")
xs66 = scr.s(i10,i26, nid="xs66")
xs67 = scr.s(i11,i27, nid="xs67")
xs66 = scr.s(i10,i26, nid="xs66")
xs67 = scr.s(i11,i27, nid="xs67")
xc68 = scr.m2(xs66,pp58, nid="m268")
xc69 = ~ scr.m2(xs66,pp58, nid="m269")
xc70 = scr.m2(xc69,~pp64, nid="m270")
xc71 = ~ scr.m2(xc69,~pp64, nid="m271")
hc44 = scr.c(i3,i21,i5, nid="hc44")
hc45 = scr.c(i2,i20,i4, nid="hc45")
xs50 = scr.s(i6,i22, nid="xs50")
xs51 = scr.s(i7,i23, nid="xs51")
xs50 = scr.s(i6,i22, nid="xs50")
xs51 = scr.s(i7,i23, nid="xs51")
xc52 = scr.m2(xs50,~hc44, nid="m252")
xc53 = ~ scr.m2(xs50,~hc44, nid="m253")
xc54 = scr.m2(xc53,~pp48, nid="m254")
xc55 = ~ scr.m2(xc53,~pp48, nid="m255")
xs60 = scr.s(i8,i24, nid="xs60")
xs61 = scr.s(i9,i25, nid="xs61")
xs60 = scr.s(i8,i24, nid="xs60")
xs61 = scr.s(i9,i25, nid="xs61")
xc72 = scr.m2(xs66,xs60, nid="m272")
xc73 = ~ scr.m2(xs66,xs60, nid="m273")
xc74 = scr.m2(xc72,xc55, nid="m274")
xc75 = ~ scr.m2(xc72,xc55, nid="m275")
xc76 = scr.m2(xc75,xc70, nid="m276")
xc77 = ~ scr.m2(xc75,xc70, nid="m277")
xs82 = scr.s(i12,i28, nid="xs82")
xs83 = scr.s(i13,i29, nid="xs83")
xs82 = scr.s(i12,i28, nid="xs82")
xs83 = scr.s(i13,i29, nid="xs83")
xc94 = scr.m2(xs88,xs82, nid="m294")
xc95 = ~ scr.m2(xs88,xs82, nid="m295")
xc118 = scr.m2(xc112,xc94, nid="m2118")
xc119 = ~ scr.m2(xc112,xc94, nid="m2119")
xc120 = scr.m2(xc118,xc77, nid="m2120")
xc121 = ~ scr.m2(xc118,xc77, nid="m2121")
xc122 = scr.m2(xc121,xc116, nid="m2122")
xc123 = ~ scr.m2(xc121,xc116, nid="m2123")
pox = [xc123]
