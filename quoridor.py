import numpy as np
import pygame as p


black = (0,0,0)
white = (255,255,255)

def gameBoard(res,x):
    pix = int(res[0]/(x+1))
    pixHoles = int(pix/8)

    for i in range(x):
        for j in range(y):  
            rect = p.Rect(i*pix+ i*pixHoles,j*pix+ j*pixHoles,pix,pix)
            p.draw.rect(screen,white,rect)
 

#screen
res = (800,800)
screen =  p.display.set_mode(res)

#gameconfig
x = 9
y = 9
squares = np.zeros((x,y))
holes = np.zeros((x-1,y-1))


gameBoard(res,x)


while 1:

    ev = p.event.get()
    for event in ev:
        if event.type == p.MOUSEBUTTONUP:
            pos = p.mouse.get_pos()
            print(pos)

    p.display.update()
    

