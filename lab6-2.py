import sys 
import pygame as pg
pg.init()
win_x = 800
win_y = 800
screen = pg.display.set_mode((win_x, win_y))
check_d = False
check_a = False
check_w = False
check_s = False
d = 0
a = 0
w = 0
s = 0
posX = 100
posY = 100
while(1):
    screen.fill((255, 255, 255))
    pg.draw.rect(screen,(100,100,100),(posX+d-a,posY-w+s,100,100))
    if check_d == True:
        print(d)
        d += 0.5
        pg.time.delay(1)
    if check_a == True:
        print(a)
        a += 0.5
        pg.time.delay(1)
    if check_w == True:
        print(w)
        w += 0.5
        pg.time.delay(1)
    if check_s == True :
        print(w)
        s += 0.5
        pg.time.delay(1)


    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
       # D Event
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            check_d = True
            print("Key d down")
        if event.type == pg.KEYUP and event.key == pg.K_d: #ปุ่มถูกปล่อยและเป็นปุ่ม D
            print("Key d up")
            check_d = False
        # A Event
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดลงและเป็นปุ่ม A
            check_a = True
            print("Key a down")
        if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key a up")
            check_a = False
        # W Event
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม W
            check_w = True
            print("Key w down")
        if event.type == pg.KEYUP and event.key == pg.K_w: #ปุ่มถูกปล่อยและเป็นปุ่ม W
            print("Key w up")
            check_w = False
        # S Event
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม S
            check_s = True
            print("Key s down")
        if event.type == pg.KEYUP and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม S
            print("Key s up")
            check_s = False