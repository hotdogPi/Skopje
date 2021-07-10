import lifelib
sess = lifelib.load_rules("b3s23")
lt = sess.lifetree(n_layers=1)

def minpop(pat):
    return min(pat[i].population for i in range(pat.period))

rect1 = lt.pattern("""8bo$7bobo$8bo2$6b5o$5bo4bo$4bo2bo$bo2bob2o$obobo5bo$bo2bo4bobo$4b2o2bo
2bo$9b2o9$17b2o$17b2o8$7b2o22b2o$8bo21bo2bo$5b3o23b2o$5bo6$14b2o$15bo$12b3o$12bo""")
rect2 = rect1("rot180",52,74)
grect = lt.pattern("bo$2o$obo")(17,23)

def rectifier_loop(p):
    if p%4 == 0 or p < 106:
        return None
    elif p%4 == 1:
        n_gliders, mpop = (2, 116) if p >= 133 else (10, 156)
    elif p%4 == 3:
        n_gliders, mpop = (6, 136)
    elif p%8 == 2:
        n_gliders = 1 if p >= 266 else 5
        mpop = 113 if p >= 266 else 133 if p >= 210 else None
    else:
        n_gliders, mpop = (3, 123 if p >= 206 else None)
    exts = (p*n_gliders - 266) // 8
    pat = rect1 + rect2(exts,exts)
    for _ in range(n_gliders):
        pat = (pat+grect)[p]
    return (pat, mpop)

p4b1 = lt.pattern("8b2o$o7bo9bo$3o3bobo7b3o$3bob3o7bo$2bob2o9b2o$2bo2bo$11bo$10bobo$3bo2bo2bo2bo$4b2o4b2o")
p4b2 = lt.pattern("b2o$2bo$2bobo$3b2o3$7b2o$6bo2bo$7bobo$o7bo$3o$3bo$2bo$2bo2bo2b2o$5bo2b2o$3bobo$2bobo$2bo$b2o")(-6,10)
p4b3 = lt.pattern("7b2o4b2o$6bo2bo3b2o$6bobo$7bo6bo$14b2o$2b2o12bo$3bo7b2o2bo$3o7bobo3b3o$o9bo7bo$9b2o")(4,25)
p4b4 = lt.pattern("7b2o$7bo$5bobo$3b2obo$6o$3o$6b2o$6bo$7b3o$bo7bo$obo$o2bo$b2o3$5b2o$5bobo$7bo$7b2o")(19,6)
gp4b = lt.pattern("2o$obo$o")(12,11)

def construct_p4_bumper_loop(p):
    if p%8 != 4 or p < 52:
        return None
    n_gliders = 1 if p >= 140 else 3
    slack = (p*n_gliders - 140) // 8
    i = 0 if p >= 140 else (p-68) // 8 if p >= 68 else (p-52) // 8
    pat = p4b1 + p4b2(-i,i) + p4b3(slack-2*i,slack) + p4b4(slack-i,slack-i)
    for _ in range(n_gliders):
        pat = (pat+gp4b)[p]
    return pat

p8b1 = lt.pattern("""x = 26, y = 27, rule = B3/S23
10b2o$10b2o$25bo$23b3o$9b3o10bo$9b2o11b2o$12b2o$11b3o4bo$10bobo4bobo$
10b2o4bo2bo$17b2o2$3b2o5b2o$4bo5b2o$4bobo$5b2o7bo$9b2ob2o$8bobo2b2o$9b
o$5bo$4b3o$3bob3o$2bo3bo$bo3bo$3obo$b3o$2bo!""")
p8b2 = lt.pattern("""x = 22, y = 28, rule = B3/S23
13bo2b2o$12bo3b2o2b2o$12bo7b2o$13b4o4$12bo$11bobo$11bo2bo$12b2o3$16b2o
$16bobo$18bo$2o16b2o$2o2b2o$4bobo$5bo$8b3o$2b2o3bo$3bo3bo3bo$3o4bo2bob
o$o8bobo2bo$10bo3bo$14bo$11b3o!""")(14,8)

def construct_p8_loop(p):
    if p%8 or p < 104:
        return None
    exts = p//8 - 13
    return p8b1 + p8b2(exts,exts)[exts%2*4]

snark1 = lt.pattern("9b2o$8bobo$2b2o4bo$o2bo2b2ob4o$2obobobobo2bo$3bobobobo$3bobob2o$4bo2$17b2o$8b2o7bo$8b2o5bobo$15b2o7$5b2o$6bo$3b3o$3bo")
snark2 = snark1("rot90",-20,30)
snark3 = snark1("rot180",10,50)
snark4 = snark1("rot270",30,20)
gsnark = lt.pattern("bo$2o$obo")(7,13)

def construct_snark_loop(p):
    if not (43 <= p < 106) or p%4 == 0:
        return None
    elif p%2:
        n_gliders = 8
        i = (p-37) // 4 if p%4 == 1 else (p-29) // 2 if p <= 75 else (p-79) // 4
    else:
        if p <= 54:
            n_gliders = 8
            i = (2,3,0)[(p-46)//4]
        else:
            n_gliders = 4
            i = (p-58) // 4
    slack = p*n_gliders//8 - 29
    pat = snark1 + snark2(-i,i) + snark3(slack-2*i,slack) + snark4(slack-i,slack-i)
    for _ in range(n_gliders):
        pat = (pat+gsnark)[p]
    return pat

p3b1 = lt.pattern("22bo$20b3o$9b3o7bo$7bo11b2o$5bobo2bo$15bo$4bob4o4bobo$3bo2b3o4bo2bo$5bo8b2o$2bo2bo$2bo$3bo$3o$o")
p3b2 = p3b1("rot90",-6,36)[2]
p3b3 = p3b1("rot180",30,42)[1]
p3b4 = p3b1("rot270",36,6)
gp3b = lt.pattern("2o$obo$o")(16,10)

def construct_p3_bumper_loop(p):
    if p%3 or p%8 == 0 or p < 36:
        return None
    if p%2:
        n_gliders = 4 if p >= 57 else 12
        i = (p-54) // 4 if p >= 57 else (15,20,24)[(p-39)//6]
    elif p%4:
        n_gliders = 2 if p >= 114 else 6
        i = (p-58) // 4 if 66 <= p <= 102 else 0
    else:
        n_gliders = 1 if p >= 228 else 3 if p >= 84 else 5 if p >= 60 else 7
        i = (0,2,0,0,2,5,8,11,0)[(p-36)//24] if p <= 228 else 2
    slack = (p*n_gliders - 220) // 8
    pat = p3b1 + p3b2(-i,i)[2*i] + p3b3(slack-2*i,slack)[2*slack] + p3b4(slack-i,slack-i)[2*slack-i]
    for _ in range(n_gliders):
        pat = (pat+gp3b)[p]
    return pat

p6b1 = lt.pattern("4b2o14bo$2o2b2o12b3o$2o2bob2o9bo$5b3o9b2o2$13bo$5b2o5bobo$5b2o4bo2bo$12b2o")
p6b2 = p6b1("rot90",-2,28)[5]
p6b3 = p6b1("rot180",26,30)[4]
p6b4 = p6b1("rot270",28,2)[3]
gp6b = lt.pattern("2o$obo$o")(14,10)

def construct_p6_bumper_loop(p):
    if p%6 or p%8 == 0 or p < 36:
        return None
    if p%4:
        n_gliders = 2 if p >= 66 else 6
        i = (p-30) // 4 if p <= 54 else 0
    else:
        n_gliders = 1 if p >= 132 else 3 if p >= 60 else 5
        i = (1,0,3,6)[(p-36)//24] if p <= 108 else 0
    slack = (p*n_gliders - 124) // 8
    pat = p6b1 + p6b2(-i,i)[2*i] + p6b3(slack-2*i,slack)[2*slack] + p6b4(slack-i,slack-i)[2*(slack+i)]
    for _ in range(n_gliders):
        pat = (pat+gp6b)[p]
    return pat

pd0_1 = lt.pattern("""x = 21, y = 21, rule = B3/S23
15b2o$15b2o9$16bo$15b3o$14b5o$13b2o3b2o$14b5o$14bo3bo$17bo$bo2b2o4b2o
4bo$o3b3o2b3o3bo2b3o$bo2b2o4b2o2bo3bo$19bo!""")
pd0_2 = lt.pattern("""x = 20, y = 20, rule = B3/S23
5bo2b2o4b2o2bo$4bo3b3o2b3o3bo$3bo4b2o4b2o2bo$2bo$bo3bo$b5o$2o3b2o$b5o$
2b3o$3bo9$3b2o$3b2o!""")(18,16)

pd15_1 = lt.pattern("""x = 50, y = 16, rule = B3/S23
24b2o$24b2o$bo2bob2obo2bo24bo2bob2obo2bo$2o2bo4bo2b2o22b2o2bo4bo2b2o$b
o2bob2obo2bo9b2o2b2o9bo2bob2obo2bo$21bobo2bobo$23bo2bo8$24b2o$24b2o!""")(-25,0)
pd15_2 = lt.pattern("""x = 21, y = 20, rule = B3/S23
11bo6bo$10b2o6b2o$9b3o6b3o$10b2o6b2o$11bo6bo2$bo$3o3$3o2$obo$obo2$3o3$
3o$bo!""")(4,11)

pd30_1 = lt.pattern("""x = 22, y = 19, rule = B3/S23
20bo$19bobo2$bo$obo16b3o$19b3o$11bo8bo$3o9bo$3o7b3o$bo18bo$9b3o7b3o$9b
o9b3o$bo8bo$3o$3o16bobo$20bo2$obo$bo!""")
pd30_2 = lt.pattern("2b2o6b2o$o4bo2bo4bo$o4bo2bo4bo$o4bo2bo4bo$2b2o6b2o")(29,25)

pd45_1 = lt.pattern("""x = 20, y = 21, rule = B3/S23
16b3o2$15bo3bo$15bo3bo2$16b3o3$16b3o2$15bo3bo$15bo3bo2$16b3o3$2o3bo2bo
3b2o$5o4b5o$2o3bo2bo3b2ob3o$15bo$16bo!""")
pd45_2 = lt.pattern("""x = 18, y = 18, rule = B3/S23
8bo6bo$7b2o6b2o$6b3o6b3o$7b2o6b2o$8bo6bo4$bo$bo$obo$bo$bo$bo$bo$obo$bo
$bo!""")(18,18)

pd60_1 = lt.pattern("17b3o$2bo2bo4bo2bo3bo$3o2b6o2b3o2bo$2bo2bo4bo2bo")
pd60_2 = lt.pattern("2bo2bo4bo2bo$3o2b6o2b3o$2bo2bo4bo2bo")(25,5)

pd75_1 = lt.pattern("""x = 22, y = 21, rule = B3/S23
20bo$19bobo3$19b3o$19b3o$20bo3$20bo$19b3o$19b3o3$19bobo$20bo$2b2o6b2o$
bo2bo4bo2bo4b3o$6o2b6o3bo$bo2bo4bo2bo5bo$2b2o6b2o!""")
pd75_2 = lt.pattern("bo2b2o4b2o2bo$o3b3o2b3o3bo$bo2b2o4b2o2bo")(26,23)

pd90_1 = lt.pattern("""x = 22, y = 21, rule = B3/S23
20bo$19bobo3$19b3o$19b3o$20bo3$20bo$19b3o$19b3o3$19bobo$20bo$2b2o6b2o$
bo2bo4bo2bo4b3o$6o2b6o3bo$bo2bo4bo2bo5bo$2b2o6b2o!""")
pd90_2 = lt.pattern("""x = 22, y = 21, rule = B3/S23
10b2o6b2o$9bo2bo4bo2bo$8b6o2b6o$9bo2bo4bo2bo$10b2o6b2o$bo$obo3$3o$3o$b
o3$bo$3o$3o3$obo$bo!""")(21,24)

p6ts1 = lt.pattern("""x = 15, y = 19, rule = B3/S23
7b2o4bo$7b2o3bobo$13bo3$2o2b2o2b2o$2o2b2ob2o$9bo3$3b2o$2bo2b2o$2bo4b2o
$2o3bob2o$bobo$bob6o$2bo5bo$3b3o$5bo!""")
p6ts2 = lt.pattern("""x = 15, y = 19, rule = B3/S23
9bo$9b3o$6bo5bo$6b6obo$11bobo$6b2o2bo2b2o$6bobo2b2o$10bobo$11bo4$9b2o
2b2o$9b2o2b2o3$bo$obo3b2o$bo4b2o!""")(13,3)

def construct_pd0_shuttle(p):
    if p%120 != 0 or p <= 0:
        return None
    return pd0_1 + pd0_2(p//120*15, p//120*15)

def construct_pd15_shuttle(p):
    if p%120 != 15 or p <= 15:
        return None
    q = pd15_2(p//120*15, p//120*15)
    return pd15_1 + q + q("flip_x",-1,0)

def construct_pd30_shuttle(p):
    if p%120 != 30 or p <= 30:
        return None
    return pd30_1 + pd30_2(p//120*15, p//120*15) + pd30_2(-50-p//120*15, -36-p//120*15)

def construct_pd45_shuttle(p):
    if p%120 != 45:
        return None
    return pd45_1 + pd45_2(p//120*15, p//120*15)

def construct_pd60_shuttle(p):
    if p%120 != 60:
        return None
    return pd60_1 + pd60_2(p//120*15, p//120*15)

def construct_pd75_shuttle(p):
    if p%120 != 75:
        return None
    return pd75_1 + pd75_2(p//120*15, p//120*15)

def construct_pd90_shuttle(p):
    if p%120 != 90:
        return None
    return pd90_1 + pd90_2(p//120*15, p//120*15)

def construct_p6thumb_shuttle(p):
    if p%24 != 18 or p < 90:
        return None
    return p6ts1 + p6ts2((p-90)//8, (p-90)//8)

tbs0_1 = lt.pattern("""x = 13, y = 35, rule = B3/S23
2b2o5b2o$2b2o5b2o6$2b3o3b3o$bo2bo3bo2bo$bo3bobo3bo$2obobobobob2o$2ob2o
3b2ob2o$b3o5b3o6$3bo$2bobo$bo3bo$b5o$obobobo$bo3bo2$bo3bo$obobobo$b5o
3b2o$bo3bo3b2o$2bobo$3bo2$2b3o$2bo$3bo!""")
tbs0_2 = lt.pattern("""x = 31, y = 13, rule = B3/S23
19b2o$18b5o$2b2o14bo4bo5b2o$2b2o14b3o2bo5b2o$19bo2b2o$20b2o$4bo3bo$2b
2obobob2o9b2o$bob2o3b2obo7bo2b2o$o2bo5bo2bo5b3o2bo5b2o$bob2o3b2obo6bo
4bo5b2o$2b2obobob2o7b5o$4bo3bo10b2o!""")(-8,10)

tbs138_1 = lt.pattern("""x = 35, y = 16, rule = B3/S23
b2o15bo3bo$b2o3b2o9bo5bo9b2o$6b2o9bo15b2o$17b2o3bo$19b3o2$b2o16b3o$o2b
o13b2o3bo$o2bo13bo15b2o$b2o14bo5bo9b2o$18bo3bo3$9b2o6bo$9bobo6b2o$9bo
7b2o!""")
tbs138_2 = lt.pattern("""x = 34, y = 11, rule = B3/S23
12bo3bo5bob2o$2o9bo5bo4bobobo$2o9bo9bo4bo$11b2o3bo5bobobo$13b3o6bob2o
2$13b3o$11b2o3bo$2o9bo15b2o$2o9bo5bo9b2o3b2o$12bo3bo15b2o!""")(-1,24)

def construct_tbs0_shuttle(p):
    if p%184 != 0 or p <= 0:
        return None
    return tbs0_1 + tbs0_2(p//184*23, p//184*23)

def construct_tbs138_shuttle(p):
    if p%184 != 138:
        return None
    return tbs138_1 + tbs138_2(p//184*23, p//184*23)