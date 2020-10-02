import numpy as np
import pygame as p

#caption and icon
p.display.set_caption("Quoridor")
icon = p.image.load("./image/gameIcon.png")
p.display.set_icon(icon)

#screen
resolution = (900,900)
screen =  p.display.set_mode(resolution)

#colors
black = (0,0,0)
redWood= (12,20,20)
emptyHole = (90,40,40)
fullHole = (193,154,107)

#images
player1 = p.image.load('./image/devil.png')
player2 = p.image.load("./image/cthulhu.png")

#gameconfig 
n = 9
offset = 10
playerOffset = 8
cells = np.zeros((n,n))
cells[5,4] = 1
cells[4,4] = 2
verHoles = np.zeros((n-1,n))
horHoles = np.zeros((n,n-1))

def drawBoard():
    n = len(cells[0])   
    pix = int((resolution[0]-2*offset)/(44))

    for i in range(n):
        for j in range(n):
            xCell = i*pix*4 + i*pix + offset
            yCell = j*pix*4 + j*pix + offset

            # Cells
            cell = p.Rect( xCell , yCell ,pix*4,pix*4)
            p.draw.rect(screen,redWood,cell)
            if cells[i,j] == 1:
                #draw player 1
                screen.blit(player1, (xCell + playerOffset, yCell + playerOffset)) 
            elif cells[i,j] == 2:
                #draw player 2         
                screen.blit(player2, (xCell + playerOffset, yCell + playerOffset))
            
            # Vertical Holes
            if i < n - 1: 
                verHole = p.Rect( xCell + 4*pix, yCell,pix,4*pix)
                if verHoles[i,j] == 1:
                    p.draw.rect(screen,fullHole,verHole)
                else:
                    p.draw.rect(screen,emptyHole,verHole)

            # Horizontal Holes
            if j < n-1:
                horHole = p.Rect( xCell, yCell+4*pix,pix*4,pix)
                if j %2 == 0:
                    p.draw.rect(screen,emptyHole,horHole)
                else :
                    p.draw.rect(screen,fullHole,horHole)

    return         
 

#Game Loop
turn = 1
running = True

screen.fill(black)
drawBoard()

p.display.update()

while running:

    events = p.event.get()
    for event in events:
        if event.type == p.QUIT:
            running = False
        if event.type == p.MOUSEBUTTONUP:
            pos = p.mouse.get_pos()
            pos = [pos[0] - offset,pos[1] - offset] 
            
            print(pos)
            

    #p.display.update()
    

