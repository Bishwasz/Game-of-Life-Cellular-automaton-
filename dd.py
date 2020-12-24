import pygame
pygame.init()

displayDimenson=700                                                  # How big do you want the display screen?
gridDimenson=35                                                     # How many boxes do you want in x and y?
width=displayDimenson/gridDimenson                                   # This will be the width of the boxes in Pixels.


win=pygame.display.set_mode((displayDimenson,displayDimenson),pygame.FULLSCREEN)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
fps=9
#   COLORS
dead=(216, 60, 255)
alive=(194, 255, 63)
neonGreen=(57,255,20)
crimson=(184,15,10)
white=(255,255,255)
blue=(20,20,250)
lineColor=(57, 255, 20)

font=pygame.font.Font(None, 24)
margin=2 # This will be the width of the grid line.

def text():
    messsage_to_screen("Welcome To Game of Life a Zero player game",neonGreen,(displayDimenson//2)-190,(displayDimenson//2)-200)
    messsage_to_screen("Game of life consists of cells on a grid",neonGreen,(displayDimenson//2)-180,(displayDimenson//2)-175)
    messsage_to_screen("and",neonGreen,(displayDimenson//2)-20,(displayDimenson//2)-155)
    messsage_to_screen("based on few rules a cell can live, multiply or die.",neonGreen,(displayDimenson//2)-180,(displayDimenson//2)-135)
    messsage_to_screen("The following rules apply to each cell:",neonGreen,(displayDimenson//2)-180,(displayDimenson//2)-111)
    messsage_to_screen("1. Each cell with one or no neighbors dies, as if by solitude.",crimson,(displayDimenson//2)-235,(displayDimenson//2)-95)
    messsage_to_screen("2. Each cell with four or more neighbors dies, as if by overpop.",crimson,(displayDimenson//2)-235,(displayDimenson//2)-75)
    messsage_to_screen("3. Each cell with two or three neighbors survives.",crimson,(displayDimenson//2)-235,(displayDimenson//2)-55)
    messsage_to_screen("4. Each cell with three neighbors becomes populated.",crimson,(displayDimenson//2)-235,(displayDimenson//2)-35)
    messsage_to_screen("A neighbour is considered as the 8 cells surrounding it.",neonGreen,(displayDimenson//2)-220,(displayDimenson//2-15))
    messsage_to_screen(" Space to pause (Black grid means it is paused)",white,25,displayDimenson-100)
    messsage_to_screen(" Press r to Reset the grid.",white,25,displayDimenson-50)
    messsage_to_screen(" Press enter or b to start.",blue,(displayDimenson//2)-60,(displayDimenson//2)+15)
    messsage_to_screen(" Press ESC to exit the window.",white,25,(displayDimenson)-75)

def messsage_to_screen(txt,color,x,y):
    message=font.render(txt, True, color)
    win.blit(message,[x,y])

def count(grid,row,col):                                             #This function reurns how many neighbours is around a given id of a grid.
    sum=0
    for x in range(-1,2):
        for y in range(-1,2):
            rows=(row+x+gridDimenson)%gridDimenson
            cols=(col+y+gridDimenson)%gridDimenson
            sum+=grid[rows][cols]
    sum-=grid[row][col]
    return sum

def drawLine():
    for l in range(gridDimenson):                                            #   Loop to draw the line
        pygame.draw.line(win,lineColor,(l*width,0),(l*width,displayDimenson),margin)
        pygame.draw.line(win,lineColor,(0,l*width),(displayDimenson,l*width),margin)

def drawGrid():
    x,y=0,0
    for row in range(gridDimenson):                                     #   Main Loop to draw the grid.
        for col in range(gridDimenson):
            if grid[row][col]==0:
                pygame.draw.rect(win,dead,(x,y,width,width))
            else:
                pygame.draw.rect(win,alive,(x,y,width,width))
            x+=width
        y+=width
        x=0

             
switch=1                                                               #   This is so you can pause.
running=True                                                         # For the main loop
menu=True

grid=[[0]*(gridDimenson) for i in range((gridDimenson))]                #   Creates an 2d array   

while running:

    while menu:
        text()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    exit()          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key ==pygame.K_b:
                    menu=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:                                               #   For the pause property. Switches between -1 and 1.
        switch *=-1
    if switch==1:  #   Main pause if
        lineColor=(0, 0, 0)
    if keys[pygame.K_r]:    # Reset
        grid=[[0]*(gridDimenson) for i in range((gridDimenson))] 

    next= [[0]*(gridDimenson) for i in range((gridDimenson))]           #  Creates a dupicate grid   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:                          #For clickable grid
            mousePos=pygame.mouse.get_pos()
            grid[round(mousePos[1]//width)][round(mousePos[0]//width)]=1
    drawGrid()
    drawLine()


    if switch==-1:  #   Main pause if
        lineColor=(255, 184, 62)
        for i in range(gridDimenson):
            for y in range(gridDimenson):
                state=grid[i][y]
                neighbours=count(grid,i,y)                                  #   Function Returns Number of Neighbours
                if state==0 and neighbours==3:                              #    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                    next[i][y]=1
                elif state==1 and( neighbours<2 or neighbours>3):           #   Any live cell with more than three live neighbours dies, as if by overpopulation. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                    next[i][y]=0
                else:
                    next[i][y]=state
        grid=next 
    clock.tick(fps)
        
        
    pygame.display.update()

