from scr.Term import *
from scr.TermTopo  import *
from scr.TermDot  import *


pp18 = Atom("pp_0_1")   # n18 --
pp20 = Atom("pp_1_0")   # n20 --
pp24 = Atom("pp_0_2")   # n24 --
pp26 = Atom("pp_1_1")   # n26 --
pp28 = Atom("pp_2_0")   # n28 --
pp46 = Atom("pp_0_3")   # n46 --
pp48 = Atom("pp_1_2")   # n48 --
pp50 = Atom("pp_2_1")   # n50 --
pp52 = Atom("pp_3_0")   # n52 --
pp86 = Atom("pp_1_3")   # n86 --
pp88 = Atom("pp_2_2")   # n88 --
pp90 = Atom("pp_3_1")   # n90 --
xc22 = scr.m2(pp20,pp18, nid="m222")
xc23 = ~ scr.m2(pp20,pp18, nid="m223")
xs34 = scr.s(pp26,pp28, nid="xs34")
xs35 = scr.s(~pp26,~pp28, nid="xs35")
xs34 = scr.s(pp26,pp28, nid="xs34")
xs35 = scr.s(~pp26,~pp28, nid="xs35")
xc38 = scr.m2(xs34,pp24, nid="m238")
xc39 = ~ scr.m2(xs34,pp24, nid="m239")
xs40 = scr.s(pp24,xs34, nid="xs40")
xs41 = scr.s(~pp24,~xs34, nid="xs41")
xs40 = scr.s(pp24,xs34, nid="xs40")
xs41 = scr.s(~pp24,~xs34, nid="xs41")
xc42 = scr.m2(~xs34,pp28, nid="m242")
xc43 = ~ scr.m2(~xs34,pp28, nid="m243")
xc44 = scr.m2(xc43,xc39, nid="m244")
xc45 = ~ scr.m2(xc43,xc39, nid="m245")
xs58 = scr.s(pp50,pp52, nid="xs58")
xs59 = scr.s(~pp50,~pp52, nid="xs59")
xs58 = scr.s(pp50,pp52, nid="xs58")
xs59 = scr.s(~pp50,~pp52, nid="xs59")
xc62 = scr.m2(xs58,pp48, nid="m262")
xc63 = ~ scr.m2(xs58,pp48, nid="m263")
xs64 = scr.s(pp48,xs58, nid="xs64")
xs65 = scr.s(~pp48,~xs58, nid="xs65")
xs64 = scr.s(pp48,xs58, nid="xs64")
xs65 = scr.s(~pp48,~xs58, nid="xs65")
xs70 = scr.s(pp46,xs64, nid="xs70")
xs71 = scr.s(~pp46,~xs64, nid="xs71")
xs70 = scr.s(pp46,xs64, nid="xs70")
xs71 = scr.s(~pp46,~xs64, nid="xs71")
xc74 = scr.m2(xs70,xc45, nid="m274")
xc75 = ~ scr.m2(xs70,xc45, nid="m275")
xs76 = scr.s(xc44,~xs70, nid="xs76")
xs77 = scr.s(xc45,xs70, nid="xs77")
xs76 = scr.s(xc44,~xs70, nid="xs76")
xs77 = scr.s(xc45,xs70, nid="xs77")
xc78 = scr.m2(xs76,xs40, nid="m278")
xc79 = ~ scr.m2(xs76,xs40, nid="m279")
xc80 = scr.m2(xc78,xc22, nid="m280")
xc81 = ~ scr.m2(xc78,xc22, nid="m281")
xc82 = scr.m2(~xs58,pp52, nid="m282")
xc83 = ~ scr.m2(~xs58,pp52, nid="m283")
xc84 = scr.m2(xc83,xc63, nid="m284")
xc85 = ~ scr.m2(xc83,xc63, nid="m285")
xs96 = scr.s(pp88,pp90, nid="xs96")
xs97 = scr.s(~pp88,~pp90, nid="xs97")
xs96 = scr.s(pp88,pp90, nid="xs96")
xs97 = scr.s(~pp88,~pp90, nid="xs97")
xs102 = scr.s(pp86,xs96, nid="xs102")
xs103 = scr.s(~pp86,~xs96, nid="xs103")
xs102 = scr.s(pp86,xs96, nid="xs102")
xs103 = scr.s(~pp86,~xs96, nid="xs103")
xs108 = scr.s(xc84,~xs102, nid="xs108")
xs109 = scr.s(xc85,xs102, nid="xs109")
xs108 = scr.s(xc84,~xs102, nid="xs108")
xs109 = scr.s(xc85,xs102, nid="xs109")
xc110 = scr.m2(~xs70,pp46, nid="m2110")
xc111 = ~ scr.m2(~xs70,pp46, nid="m2111")
xc112 = scr.m2(xc111,xc75, nid="m2112")
xc113 = ~ scr.m2(xc111,xc75, nid="m2113")
xs118 = scr.s(xs108,xc113, nid="xs118")
xs119 = scr.s(~xs108,xc112, nid="xs119")
xs118 = scr.s(xs108,xc113, nid="xs118")
xs119 = scr.s(~xs108,xc112, nid="xs119")
xs124 = scr.s(xc80,xs118, nid="xs124")
xs125 = scr.s(xc81,~xs118, nid="xs125")
xs124 = scr.s(xc80,xs118, nid="xs124")
xs125 = scr.s(xc81,~xs118, nid="xs125")
pox = [xs124]
