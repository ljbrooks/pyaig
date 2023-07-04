from scr.Term import *
from scr.TermTopo  import *
from scr.TermDot  import *


pp22 = Atom("pp_0_1")   # n22 --
pp24 = Atom("pp_1_0")   # n24 --
pp28 = Atom("pp_0_2")   # n28 --
pp30 = Atom("pp_1_1")   # n30 --
pp32 = Atom("pp_2_0")   # n32 --
pp48 = Atom("pp_1_2")   # n48 --
pp50 = Atom("pp_2_1")   # n50 --
pp52 = Atom("pp_3_0")   # n52 --
pp74 = Atom("pp_0_3")   # n74 --
pp90 = Atom("pp_0_4")   # n90 --
pp92 = Atom("pp_1_3")   # n92 --
pp100 = Atom("pp_2_2")   # n100 --
pp102 = Atom("pp_3_1")   # n102 --
pp104 = Atom("pp_4_0")   # n104 --
xc26 = scr.c(pp24,pp22, nid="xc26")
xc27 = scr.c(~pp24,~pp22, nid="xc27")
xs38 = scr.s(pp30,pp32, nid="xs38")
xs39 = scr.s(~pp30,~pp32, nid="xs39")
xs38 = scr.s(pp30,pp32, nid="xs38")
xs39 = scr.s(~pp30,~pp32, nid="xs39")
xs44 = scr.s(pp28,xs38, nid="xs44")
xs45 = scr.s(~pp28,~xs38, nid="xs45")
xs44 = scr.s(pp28,xs38, nid="xs44")
xs45 = scr.s(~pp28,~xs38, nid="xs45")
xc46 = scr.c(xs44,xc26, nid="xc46")
xc47 = scr.c(~xs44,xc27, nid="xc47")
xs58 = scr.s(pp50,pp52, nid="xs58")
xs59 = scr.s(~pp50,~pp52, nid="xs59")
xs58 = scr.s(pp50,pp52, nid="xs58")
xs59 = scr.s(~pp50,~pp52, nid="xs59")
xs64 = scr.s(pp48,xs58, nid="xs64")
xs65 = scr.s(~pp48,~xs58, nid="xs65")
xs64 = scr.s(pp48,xs58, nid="xs64")
xs65 = scr.s(~pp48,~xs58, nid="xs65")
hc72 = scr.c(~pp32,~pp28,~pp30, nid="hc72")
hc73 = scr.c(pp32,pp28,pp30, nid="hc73")
xs80 = scr.s(hc72,~pp74, nid="xs80")
xs81 = scr.s(~hc72,pp74, nid="xs81")
xs80 = scr.s(hc72,~pp74, nid="xs80")
xs81 = scr.s(~hc72,pp74, nid="xs81")
xs86 = scr.s(xs64,xs80, nid="xs86")
xs87 = scr.s(~xs64,~xs80, nid="xs87")
xs86 = scr.s(xs64,xs80, nid="xs86")
xs87 = scr.s(~xs64,~xs80, nid="xs87")
xc88 = scr.c(xs86,xc46, nid="xc88")
xc89 = scr.c(~xs86,xc47, nid="xc89")
xs98 = scr.s(pp90,pp92, nid="xs98")
xs99 = scr.s(~pp90,~pp92, nid="xs99")
xs98 = scr.s(pp90,pp92, nid="xs98")
xs99 = scr.s(~pp90,~pp92, nid="xs99")
xs110 = scr.s(pp102,pp104, nid="xs110")
xs111 = scr.s(~pp102,~pp104, nid="xs111")
xs110 = scr.s(pp102,pp104, nid="xs110")
xs111 = scr.s(~pp102,~pp104, nid="xs111")
xs116 = scr.s(pp100,xs110, nid="xs116")
xs117 = scr.s(~pp100,~xs110, nid="xs117")
xs116 = scr.s(pp100,xs110, nid="xs116")
xs117 = scr.s(~pp100,~xs110, nid="xs117")
hc124 = scr.c(~pp48,~pp50,~pp52, nid="hc124")
hc125 = scr.c(pp48,pp50,pp52, nid="hc125")
xs130 = scr.s(xs116,~hc124, nid="xs130")
xs131 = scr.s(~xs116,hc124, nid="xs131")
xs130 = scr.s(xs116,~hc124, nid="xs130")
xs131 = scr.s(~xs116,hc124, nid="xs131")
xs136 = scr.s(xs98,xs130, nid="xs136")
xs137 = scr.s(~xs98,~xs130, nid="xs137")
xs136 = scr.s(xs98,xs130, nid="xs136")
xs137 = scr.s(~xs98,~xs130, nid="xs137")
hc144 = scr.c(~xs64,hc72,~pp74, nid="hc144")
hc145 = scr.c(xs64,~hc72,pp74, nid="hc145")
xs150 = scr.s(xs136,~hc144, nid="xs150")
xs151 = scr.s(~xs136,hc144, nid="xs151")
xs150 = scr.s(xs136,~hc144, nid="xs150")
xs151 = scr.s(~xs136,hc144, nid="xs151")
xs156 = scr.s(xc88,xs150, nid="xs156")
xs157 = scr.s(xc89,~xs150, nid="xs157")
xs156 = scr.s(xc88,xs150, nid="xs156")
xs157 = scr.s(xc89,~xs150, nid="xs157")
pox = [xs156]
