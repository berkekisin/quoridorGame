import numpy as np
import pygame as p

global turn

#caption and icon
p.display.set_caption("Quoridor")
icon = p.image.load("./image/gameIcon.png")
p.display.set_icon(icon)

#screen
resolution = (1080-220,900-220)
resolution = (1080,900)
#resolution = (1080-220,900-220)
screen =  p.display.set_mode(resolution)

#colors
black = (0,0,0)
redWood= (12,20,20)
emptyHole = (90,40,40)
wallColor = (193,154,107)

#images
player1 = p.image.load('./image/devil.png')
player2 = p.image.load("./image/cthulhu.png")

trans1 = p.image.load("./image/transDevil.png")
trans2 = p.image.load("./image/transCthulhu.png")
tImages = [trans1,trans2]

#addButton = p.image.load("./image/add-button.png")

#gameconfig 
n = 9
offset = 10
playerOffset = 8
pix = int((resolution[1]-2*offset)/(44))
cells = np.zeros((n,n))
cells[0,4] = 1
cells[-1,4] = 2
playerPos= [4,76]
playerMoves = [[3,5,13],[75,77,67]]
verHoles = np.zeros((n,n-1))
horHoles = np.zeros((n-1,n))
points = np.zeros((n-1,n-1))
wallMode = True

#TODo: Bfs for both players
def BFS(id):
    player = id%2 +1
    num = ((id-1) % 2)*72
    discovered = []
    q = []
    discovered.append(playerPos[player-1])
    q.append(playerPos[player-1])

    while q:
        current = q.pop(0)

        if current >= num and current < (9 + num):
            print("find routeeeeeeeee!!!!")
            print(horHoles)
            print(verHoles)
            print(player,len(discovered),discovered)
            return True 

        for move in allMoves(current,player):

            if move not in discovered:
                q.append(move)
                discovered.append(move)
    print("UNVALIDD mOVEEEEEEEEEEEEEEEEEEEEEEE")
    print(player,len(discovered),discovered)
    print(horHoles)
    print(verHoles)
    return False 

def allMoves(pos,player):
    result = []

    x,y = calculateIndex(pos) 
    #right
    if x +1 <= n-1 and verHoles[y,x] == 0:
        if cells[y,x+1] == 0:
            move = (x+1) + y*9
            result.append(move)
    #left
    if x -1 >= 0 and verHoles[y,x-1] == 0:
        if cells[y,x-1] == 0:
            move = (x-1) + y*9
            result.append(move)       
    #down 
    if y +1 <= n-1 and horHoles[y,x] == 0:
        if cells[y+1,x] == 0:
            move = x + (y+1)*9
            result.append(move)
    if y -1 >= 0 and horHoles[y-1,x] == 0:
        if cells[y-1,x] == 0:
            move = x + (y-1)*9
            result.append(move)   

    return result               

def findPossibleMoves():

    for i in range(2):
        playerMoves[i].clear()
        x,y = calculateIndex(playerPos[i]) 
        #right
        if x +1 <= n-1 and verHoles[y,x] == 0:
            if cells[y,x+1] == 0:
                move = (x+1) + y*9
                playerMoves[i].append(move)
            elif cells[y,x+1] ==  ((i+1)%2 +1) and verHoles[y,x+1] == 0 and  x + 2 <= n-1:
                move = (x+2) + y*9
                playerMoves[i].append(move)
        #left
        if x -1 >= 0 and verHoles[y,x-1] == 0:
            if cells[y,x-1] == 0:
                move = (x-1) + y*9
                playerMoves[i].append(move)
            elif cells[y,x-1] ==  ((i+1)%2 +1) and verHoles[y,x-2] == 0 and  x - 2 >= 0:
                move = (x-2) + y*9
                playerMoves[i].append(move)        
        #down 
        if y +1 <= n-1 and horHoles[y,x] == 0:
            if cells[y+1,x] == 0:
                move = x + (y+1)*9
                playerMoves[i].append(move)
            elif cells[y+1,x] ==  ((i+1)%2 +1) and horHoles[y+1,x] == 0 and y + 2 <= n-1:
                move = x + (y+2)*9
                playerMoves[i].append(move)
        #up
        if y -1 >= 0 and horHoles[y-1,x] == 0:
            if cells[y-1,x] == 0:
                move = x + (y-1)*9
                playerMoves[i].append(move)
            elif cells[y-1,x] == ((i+1)%2 +1) and horHoles[y-2,x] == 0 and y - 2 >= 0:
                move = x + (y-2)*9
                playerMoves[i].append(move)   

    return playerMoves
    
def calculateIndex(pos):
    x = pos % n
    y= pos // 9

    return x,y

#calculates pixels of pos
def calculatePos(pos):
    x = pos % n
    y= pos // 9

    xx = x*pix*4 + x*pix + offset*10
    yy = y*pix*4 + y*pix + offset

    return xx,yy

def deleteTransPicturens():
    for i in playerMoves[turn -1]:
        a,b = calculatePos(i)
        box = p.Rect(a , b ,pix*4,pix*4)
        p.draw.rect(screen,redWood,box)

def drawBoard(): 

    #button = p.Rect(resolution[0] - 40,resolution[1] - 40,40,40)
    #p.draw.rect(screen,redWood,button)
    #screen.blit(addButton, (resolution[0] - 64, resolution[1] - 64))
    
    background = p.Rect( offset*10 , offset ,resolution[1]-2*offset,resolution[1]-2*offset)
    p.draw.rect(screen,emptyHole,background)
    
    for i in range(n):
        for j in range(n):

            num = j*9 + i
            xCell,yCell = calculatePos(num)

            # Cells
            cell = p.Rect( xCell , yCell ,pix*4,pix*4)
            p.draw.rect(screen,redWood,cell)
            
            # Vertical Holes
            if j < n - 1: 
                verHole = p.Rect( xCell + 4*pix, yCell,pix,4*pix)
                if verHoles[i,j] == 1:
                    p.draw.rect(screen,wallColor,verHole)

            # Horizontal Holes
            if i < n-1:
                horHole = p.Rect( xCell, yCell+4*pix,pix*4+ pix,pix)
                if horHoles[i,j] == 1:
                    p.draw.rect(screen,wallColor,horHole)

    return         

def drawPossibleMoves():

    for move in playerMoves[turn-1]:
        x,y = calculatePos(move)
        screen.blit(tImages[turn -1], (x + playerOffset, y + playerOffset))

def drawPlayer():
    x1,y1 = calculatePos(playerPos[0])
    x2,y2 = calculatePos(playerPos[1])

    screen.blit(player1, (x1 + playerOffset, y1 + playerOffset))
    #screen.blit(trans1, (xCell + playerOffset + 4*pix, yCell + playerOffset))  
    screen.blit(player2, (x2 + playerOffset, y2 + playerOffset))
    
    return
  
def handleClick(pos):

    pos = [pos[0] - offset*10,pos[1] - offset]         
    a = pos[0]//20
    b = pos[1]//20
    x = a//5
    y = b//5
    num = y*9 + x
    
    if  x < 9 and x > -1 :
        
        if a % 5 < 4:
            if b % 5 < 4:
                print("u clicked square:", x,y)
                if num in playerMoves[turn-1]:
                    handleMove(x,y)
            else:
                print("u clicked horHole:", x,y)     
                if wallMode and x<8 and horHoles[y,x] == 0  and horHoles[y,x+1] == 0 and points[y,x] == 0:
                    horHoles[y,x:x+2] = 1
                    points[y,x] = 1
                    if BFS(1) and BFS(2):
                        placeHorWall(num)
                    else:    
                        horHoles[y,x:x+2] = 0
                        points[y,x] = 0
                    
        else:
            if b%5 < 4:
                print("u clicked verHole:", x,y)
                if wallMode and y<8 and verHoles[y,x] == 0  and verHoles[y+1,x] == 0 and points[y,x] == 0:
                    verHoles[y:y+2,x] = 1
                    points[y,x] = 1
                    if BFS(1) and BFS(2):
                        placeVerWall(num)
                    else:    
                        print("UNVALIDD mOVEEEEEEEEEEEEEEEEEEEEEEE")
                        verHoles[y:y+2,x] = 0
                        points[y,x] = 0
                        
                    
            else:
                print("false click")

    return

def placeHorWall(location):
    px,py = calculatePos(location)
    x,y = calculateIndex(location)
    horWall= p.Rect( px , py+ 4*pix,2*4*pix + pix,pix)
    p.draw.rect(screen,wallColor,horWall)
    horHoles[y,x:x+2] = 1
    points[y,x] = 1
    deleteTransPicturens()
    global turn
    player = turn
    turn = player%2 +1
    findPossibleMoves()
    drawPossibleMoves()
    return

def placeVerWall(location):
    px,py = calculatePos(location)
    x,y = calculateIndex(location)
    verWall= p.Rect( px + 4*pix, py,pix ,2*4*pix+ pix)
    p.draw.rect(screen,wallColor,verWall)
    verHoles[y:y+2,x] = 1
    points[y,x] = 1
    deleteTransPicturens()
    global turn
    player = turn
    turn = player%2 +1
    findPossibleMoves()
    drawPossibleMoves()
    return

def handleMove(x,y):
    deleteTransPicturens()

    global turn 
    num = playerPos[turn-1]
    oldX, oldY = calculateIndex(num)  
    cells[oldY,oldX] = 0
    cells[y,x] = turn
    playerPos[turn-1] = x + y*n

    xCell,yCell = calculatePos(num)
    cell = p.Rect( xCell , yCell ,pix*4,pix*4)
    p.draw.rect(screen,redWood,cell)

    drawPlayer()
    findPossibleMoves()

    player = turn
    turn = player%2 +1
    drawPossibleMoves()

    #print(cells)

    return 

#Game Loop
running = True
turn = 1
screen.fill(black)
drawBoard()
drawPlayer()
drawPossibleMoves()

while running:

    events = p.event.get()
    for event in events:
        if event.type == p.QUIT:
            running = False
        if event.type == p.MOUSEBUTTONUP:
            pos = p.mouse.get_pos()
            handleClick(pos)    
            
    p.display.update()
    

