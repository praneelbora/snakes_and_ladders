import pygame
import random
import time
WIDTH, HEIGHT = 700,700
BG = (255,255,255)
BLACK=(0,0,0)
FPS=4
GAME = pygame.display.set_mode((WIDTH,HEIGHT))
BACK = pygame.image.load("Assets/img2.jpeg")
BACK = pygame.transform.scale(BACK,(WIDTH,HEIGHT))
NEXT_TURN=pygame.USEREVENT +1
GOTI_B = pygame.image.load("Assets/goti_blue.png")
GOTI_B = pygame.transform.scale(GOTI_B,(50,50))
GOTI_G = pygame.image.load("Assets/goti_green.png")
GOTI_G = pygame.transform.scale(GOTI_G,(50,50))
GOTI_R = pygame.image.load("Assets/goti_red.png")
GOTI_R = pygame.transform.scale(GOTI_R,(50,50))
GOTI_Y = pygame.image.load("Assets/goti_yellow.png")
GOTI_Y = pygame.transform.scale(GOTI_Y,(50,50))
GOTIS=[GOTI_B,GOTI_G,GOTI_R,GOTI_Y]

gotis=[]
clock = pygame.time.Clock()
move=[]
def draw():
    GAME.blit(BACK,(0,0))
    for i in range(len(gotis)):
        GAME.blit(GOTIS[i],(gotis[i].x,gotis[i].y))
    pygame.display.update()


def move_goti(goti,move,num):
    move[num][2]=rand()
    for i in range(move[num][2]):
        move[num][1]+=1
        if(move[num][0]==1 and goti.x<640):
            goti.x+=70
            move[num][0]= 1
        elif(move[num][0]==1 and goti.x==640):
            goti.y-=70
            move[num][0]= -1
        elif(move[num][0]==-1 and goti.x>10):
            goti.x-=70
            move[num][0]= -1
        elif(move[num][0]==-1 and goti.x==10):
            goti.y-=70
            move[num][0]= 1
        if(move[num][1]>=100):
            move[num][0]=0
        draw()
        clock.tick(FPS*10)
    


def rand():
    val=int(random.random()*6)
    return (val if (val>0) else rand())


def check_ladder():
    for i in range(len(gotis)):
        print(move[i][1]," - x - ",gotis[i].x," - y - ",gotis[i].y)

        if(move[i][1]<100):
            if(move[i][1]==1):   # at 1
                gotis[i].y-=(70*3)
                gotis[i].x+=(70*2)
                move[i][0]=-1
                move[i][1]=38
            elif(move[i][1]==4): # at 4
                gotis[i].y-=(70*1)
                gotis[i].x+=(70*3)
                move[i][0]=-1
                move[i][1]=14
            elif(move[i][1]==9): # at 9
                gotis[i].y-=(70*3)
                gotis[i].x+=(70*1)
                move[i][0]=-1
                move[i][1]=31
            elif(move[i][1]==21): # at 21
                gotis[i].y-=(70*2)
                gotis[i].x+=(70*3)
                move[i][1]=42
            elif(move[i][1]==28): # at 28
                gotis[i].y-=(70*6)
                gotis[i].x-=(70*4)
                move[i][1]=84
            elif(move[i][1]==51): # at 51
                gotis[i].y-=(70*1)
                gotis[i].x-=(70*3)
                move[i][0]=1
                move[i][1]=67
            elif(move[i][1]==80): # at 80
                gotis[i].y-=(70*2)
                gotis[i].x+=(70*0)
                move[i][1]=100
            elif(move[i][1]==71): # at 71
                gotis[i].y-=(70*2)
                gotis[i].x+=(70*0)
                move[i][1]=91
        print(move[i][1]," - x - ",gotis[i].x," - y - ",gotis[i].y,"\n")

def check_snakes():
    for i in range(len(gotis)):
        if(move[i][1]<100):
            if(gotis[i].y==(640-70*0) and gotis[i].x==(10+70*0)):   # at 1
                gotis[i].y-=(70*3)
                gotis[i].x+=(70*2)
                move[i][0]=-1
                move[i][1]=37
            elif(gotis[i].y==(640-70*0) and gotis[i].x==(10+70*3)): # at 4
                gotis[i].y-=(70*1)
                gotis[i].x+=(70*3)
                move[i][0]=-1
                move[i][1]=14
            elif(gotis[i].y==(640-70*0) and gotis[i].x==(10+70*8)): # at 9
                gotis[i].y-=(70*3)
                gotis[i].x+=(70*1)
                move[i][0]=-1
                move[i][1]=31
            elif(gotis[i].y==(640-70*2) and gotis[i].x==(10+70*0)): # at 21
                gotis[i].y-=(70*1)
                gotis[i].x+=(70*3)
                move[i][1]=42
            elif(gotis[i].y==(640-70*2) and gotis[i].x==(10+70*7)): # at 28
                gotis[i].y-=(70*6)
                gotis[i].x-=(70*4)
                move[i][1]=84
            elif(gotis[i].y==(640-70*5) and gotis[i].x==(10+70*9)): # at 51
                gotis[i].y-=(70*1)
                gotis[i].x-=(70*3)
                move[i][0]=1
                move[i][1]=67
            elif(gotis[i].y==(640-70*7) and gotis[i].x==(10+70*0)): # at 80
                gotis[i].y-=(70*2)
                gotis[i].x+=(70*0)
                move[i][1]=100
            elif(gotis[i].y==(640-70*7) and gotis[i].x==(10+70*9)): # at 71
                gotis[i].y-=(70*2)
                gotis[i].x+=(70*0)
                move[i][1]=91

def main():
    move.append([1,0,1])
    move.append([1,0,1])
    # move[][0] helps in adding or subtracting values of goti.x
    # move[][1] helps stopping goti at 100 position
    # move[][2] says how many steps to be taken by that goti
    running = True
    GAME.fill(BG)
    goti_b=pygame.Rect(-60,640,50,50)
    goti_g=pygame.Rect(-60,640,50,50)
    gotis.append(goti_b)
    # gotis.append(goti_g) 
    turn=0
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    move_goti(goti_b,move,0) if (turn%len(gotis)==0) else move_goti(goti_g,move,1)
                    check_ladder()
                    turn+=1
            if event.type == pygame.QUIT:
                running=False
        keypress = pygame.key.get_pressed()
        draw()  
    pygame.quit()

main()