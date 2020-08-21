import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    """This creates all the walls in room 1"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map1 = """---------------
m-m-------------m---
m-m-------------m---
m-mmmmmmmmmmmkkkkkkk
m------------------m
mm-------mm---kk---m
m----pp-----------pp
p--m-----mk---km---p
p------pkm---------p
p------------mm----p
kkk--kkk--mm------kk
k------------p-----k
k-----mmm-------m---
k--mm-----------m---
kkkkkkkkkkkkkkkkkkkk""".splitlines()

    game_map = [list(lst) for lst in game_map1]

    tl = {}
    tl["p"] = pygame.image.load('square_purple.png')
    tl["m"] = pygame.image.load('square_blue.png')
    tl["k"] = pygame.image.load('square_yellow.png')


class Room2(Room):
    
    game_map2 = """
d------------------d
d------------------d
drrrrrrrrrrdddrrrrrd
dr---bb-----bbbrrrrd
d-----------------dd
d-----rbr--------rdd
d------------------d
d----rrryy---------d
d------------------d
dbb----------------d
--------rb---rr---bd
----bbb--------rr---
--------------------
rrrrrrrrrrrrrrrrrrrr
    """.splitlines()

    game_map = [list(lst) for lst in game_map2]

    tl = {}
    tl["r"] = pygame.image.load('stalactite_red.png')
    tl["b"] = pygame.image.load('stalactite_blue.png')
    tl["d"] = pygame.image.load('stalactite_red2.png')
    tl["a"] = pygame.image.load('stalactite_blue2.png')



class Room3(Room):

    game_map3 = """
--------------------
--------------------
baaaaaaaaaaaaaaaaaaa
bb--o-----a--------b
bm----------------ab
bm----bbbb--------ab
b----aaaaaaam-----bb
b---aaaaammmma----bb
b--------------aa-bb
baaaaaa---aa------bb
bm-----------aa--bbb
-----mmmmmmm---aaaae
--aa--------ab------
aaaaaaaaaaaaaaaa-aaa
    """.splitlines()

    game_map = [list(lst) for lst in game_map3]

    tl = {}
    tl["b"] = pygame.image.load('flower_blue.png')
    tl["m"] = pygame.image.load('flower_purple.png')
    tl["a"] = pygame.image.load('flower_white.png')
    tl["e"] = pygame.image.load('exit.png')

class Room4(Room):

    game_map4 = """
--------------------
--------------------
oooooooooooooooooooo
k------------------k
km----------mm-----k
k----pp-----------ok
k--m-----ok---km---k
k------pkm---------k
k------------mm----k
koo--kko--mm------kk
k------------p-----k
k-----mmm-------m---
---pp-----------m---
pppppppppppppppppppp""".splitlines()

    game_map = [list(lst) for lst in game_map4]

    tl = {}
    tl["k"] =  pygame.image.load('polygon_yellow.png')
    tl["m"] =  pygame.image.load('polygon_blue.png')
    tl["p"] =  pygame.image.load('polygon_blue2.png')
    tl["o"] =  pygame.image.load('polygon_red.png')

class Room5(Room):

    game_map5 = """
c-------------------
t------------------c
cccccccccccctttttttt
t------h-----------t
tt-----------c-----c
t---t------t-------t
c------------------t
c----tctctccttctt--c
c------------------t
t---------h--------c
tc-h------------h--t
t----ccttct--------t
-------------------c
cccccccccccccccccccc
    """.splitlines()

    game_map = [list(lst) for lst in game_map5]

    tl = {}
    tl["c"] =  pygame.image.load('circle_yellow.png')
    tl["t"] =  pygame.image.load('circle_purple.png')
    tl["h"] =  pygame.image.load('generator.png')

class Room6(Room):

    game_map6 = """aaa------------a-aaa
aaa----------------a
a-----------------aa
a------rrrr--------a
ab---bb-----bbbrrrra
d------------------a
d-----bbr--------raa
a------------------d
a----rrrbb---------a
a------------------a
dbb----------------a
a-------br---bb---ra
a---rrr--------rr--a
a------------------a
rrrrrrrrrrrrrrrrr--r
        """.splitlines()

    game_map = [list(lst) for lst in game_map6]

    tl = {}
    tl["r"] =  pygame.image.load('stalactite_red.png')
    tl["b"] =  pygame.image.load('stalactite_blue.png')
    tl["d"] =  pygame.image.load('stalactite_red2.png')
    tl["a"] =  pygame.image.load('stalactite_blue2.png')

class Room7(Room):

    game_map7 = """s------------------s
s------------------s
ssssssssssssssss---s
s------------------s
sx----------sss----x
x------------------x
x----------------xxx
s------------------x
x------------------s
q------------------s
qq-----------------s
q-----------------sq
q---ssq----s--q----q
q------------------q
qqqqsssxxqqsxsxqx--s
        """.splitlines()

    game_map = [list(lst) for lst in game_map7]

    tl = {}
    tl["s"] = pygame.image.load('lines_yellow.png')
    tl["x"] = pygame.image.load('lines_purple.png')
    tl["q"] = pygame.image.load('lines_red.png')


class Room8(Room):

    game_map8 = """s------------------s
s--------------s--ss
s--------------s---s
sxx----------------s
sx---xx------------x
x------------------x
x----xxs---------xxx
s----------ss------x
x----xx------------s
q------------------s
qq-ss--------------s
q------sx---------sq
----ssq----s--q-----
--------------------
qqqqsssxxqqsxsxqxqqs
        """.splitlines()

    game_map = [list(lst) for lst in game_map8]

    tl = {}
    tl["s"] =  pygame.image.load('lines_purple.png')
    tl["x"] = pygame.image.load('lines_yellow.png')
    tl["q"] =  pygame.image.load('lines_red.png')
    
class Room9(Room):

    game_map9 = """
mm-----------------m
mm-----------------m
mkkkkkmmmkkkmmmppppp
m------------------k
mm-------mm---kk---k
m----pp-----------kk
p--m-----mk---km---k
p------pkm---------k
p------------kk----k
kkk--mmm--pp------kk
-------------m-----k
------mmm-------m--k
--- mm--------m--mmk
mk-mkpmkpmkpmkpmkpmk
        """.splitlines()

    game_map = [list(lst) for lst in game_map9]

    tl = {}
    tl["p"] =  pygame.image.load('square_purple.png')
    tl["m"] =  pygame.image.load('square_blue.png')
    tl["k"] =  pygame.image.load('square_yellow.png')


class Room10(Room):

    game_map10 = """a-----------------a
a-------------------
a-------------------
aa-----bbbaaabbaamma
bb--o-----a--------a
bm----------------ma
bm----bbbb--------ma
b-----aabba-------aa
b----ab-----------ma
b--------------bb-ma
ba--------aa------bb
bm-----------aa--amm
b----mmmmmmm---eaaea
b-aa--------ba-----a
b-bbbbbbbbbbbbbbbbbb
    """.splitlines()

    game_map = [list(lst) for lst in game_map10]

    tl = {}
    tl["b"] = pygame.image.load('flower_blue.png')
    tl["m"] = pygame.image.load('flower_purple.png')
    tl["a"] = pygame.image.load('flower_white.png')


class Room11(Room):
 
    game_map11 = """a-----------------a
d-d----------------bd
d-d-------------bb-d
d-dddddbbbbbbbbbbbbd
d----rr------------d
-----r------------dd
------bbr--------rdd
-------------z-----d
-----rrryy---------d
-------------------d
dbb--------z-------d
d------------rr----d
----rbr--------rr--d
-------------------d
rrrrrrrrrrbrbrbrbbbr
    """.splitlines()

    game_map = [list(lst) for lst in game_map11]

    tl = {}
    tl["r"] =  pygame.image.load('stalactite_red.png')
    tl["b"] =  pygame.image.load('stalactite_blue.png')
    tl["d"] =  pygame.image.load('stalactite_red2.png')
    tl["a"] =  pygame.image.load('stalactite_blue2.png')
    tl["z"] =  pygame.image.load('generator.png')

class Room12(Room):
 
    game_map12 = """
d------------------d
d------------------d
d------bbbb--------d
dr---rr-----bbbrrrrd
-----r------------dd
------bbr-----------
-------------z------
-----rrryy----------
d-------------------
dbb--------z-------d
-------------rr----d
---------------rr---
dd---bb--rr--bb-----
dddddddddddddddddddd
    """.splitlines()

    game_map = [list(lst) for lst in game_map12]

    tl = {}
    tl["r"] =  pygame.image.load('stalactite_red.png')
    tl["b"] =  pygame.image.load('stalactite_blue.png')
    tl["d"] =  pygame.image.load('stalactite_red2.png')
    tl["a"] =  pygame.image.load('stalactite_blue2.png')
    tl["z"] =  pygame.image.load('generator.png')
    
class Room13(Room):

    game_map13 = """q------------------s
qq----------------ss
q--q------------xsss
ss-----------------s
ss--xxx-----sss----x
x--s----------------
x--xxs--x--------xx-
s--------ss---------
x------xx---x-------
q------------------s
qq-ss----------x--ss
q------sx---x-------
q---ssq----s--q-----
q------------------s 
sssssssxxqqsxsxqxqqs
        """.splitlines()

    game_map = [list(lst) for lst in game_map13]

    tl = {}
    tl["s"] =  pygame.image.load('lines_yellow.png')
    tl["x"] =  pygame.image.load('lines_purple.png')
    tl["q"] =  pygame.image.load('lines_red.png')
    
class Room14(Room):

    game_map14 = """s------------------s
s------------------s
ss-----------------s
sss---------------ss
ss--xxx-----sss----x
x--s----xxx--------x
x----xxs---------xxx
s--------ss--qq----x
x----xx------------s
q-----------sssss--s
qq-ss--------------s
q------sx---qqqq--sq
q---ssq----s--q----s
q------------------s
q--ssssxxqqsxsxqxq-s
        """.splitlines()

    game_map = [list(lst) for lst in game_map14]

    tl = {}
    tl["s"] = pygame.image.load('lines_yellow.png')
    tl["x"] = pygame.image.load('lines_purple.png')
    tl["q"] = pygame.image.load('lines_red.png')

class Room15(Room):

    game_map15 = """
--------------------
--------------------
ssssssssssssssssssss
ss--xxx-----sss----x
x--s---------------x
x----xxs---------xxx
s--------ss--------x
x----xx------------s
q------------------s
qq-ss-------------ss
q------sx---------sq
q---ssq----s--q-----
q-------------------
q--ssssxxqqsxsxqxqqs
        """.splitlines()

    game_map = [list(lst) for lst in game_map15]

    tl = {}
    tl["s"] = pygame.image.load('lines_yellow.png')
    tl["x"] = pygame.image.load('lines_purple.png')
    tl["q"] = pygame.image.load('lines_red.png')

