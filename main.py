import pygame
import random

WIDTH, HEIGHT = 700,700
BG = (255,255,255)
BLACK=(0,0,0)
FPS=1

GAME = pygame.display.set_mode((WIDTH,HEIGHT))
BACK = pygame.image.load("Assets/Boards/img2.jpeg")
BACK = pygame.transform.scale(BACK,(WIDTH,HEIGHT))
NEXT_TURN=pygame.USEREVENT +1

GOTI_B = pygame.image.load("Assets/Goti/goti_blue.png")
GOTI_B = pygame.transform.scale(GOTI_B,(50,50))
GOTI_G = pygame.image.load("Assets/Goti/goti_green.png")
GOTI_G = pygame.transform.scale(GOTI_G,(50,50))
GOTI_R = pygame.image.load("Assets/Goti/goti_red.png")
GOTI_R = pygame.transform.scale(GOTI_R,(50,50))
GOTI_Y = pygame.image.load("Assets/Goti/goti_yellow.png")
GOTI_Y = pygame.transform.scale(GOTI_Y,(50,50))
GOTIS=[GOTI_B,GOTI_G,GOTI_R,GOTI_Y]


clock = pygame.time.Clock()
move=[]
gotis=[]
# move[i][0] helps in adding or subtracting values of goti.x
# move[i][1] helps stopping goti at 100 position
# move[i][2] says how many steps to be taken by that goti

def draw():
    GAME.blit(BACK,(0,0))
    for i in range(len(gotis)):
        GAME.blit(GOTIS[i],(gotis[i].x,gotis[i].y))
    pygame.display.update()

def move_goti(goti,move):
    if move[0]!=0:
        move[2]=rand()
        print(move[1]," - x - ",goti.x," - y - ",goti.y," - ",move[2])
        for i in range(move[2]):
            if(move[1]<100):
                move[1]+=1
                if(move[0]==1 and goti.x<640):
                    goti.x+=70
                    move[0]= 1
                elif(move[0]==1 and goti.x==640):
                    goti.y-=70
                    move[0]= -1
                elif(move[0]==-1 and goti.x>10):
                    goti.x-=70
                    move[0]= -1
                elif(move[0]==-1 and goti.x==10):
                    goti.y-=70
                    move[0]= 1
                if(move[1]==100):
                    move[0]=0
                draw()
                clock.tick(FPS*10)
            else:
                return 1
        check_ladder(goti,move)
        check_snakes(goti,move)

def rand():
    val=int(random.random()*6)
    return (val if (val>0) else rand())

def check_ladder(goti,move):
    if(move[1]<100):
        if(move[1]==1):   # at 1
            goti.y-=(70*3)
            goti.x+=(70*2)
            move[0]=-1
            move[1]=38
        elif(move[1]==4): # at 4
            goti.y-=(70*1)
            goti.x+=(70*3)
            move[0]=-1
            move[1]=14
        elif(move[1]==9): # at 9
            goti.y-=(70*3)
            goti.x+=(70*1)
            move[0]=-1
            move[1]=31
        elif(move[1]==21): # at 21
            goti.y-=(70*2)
            goti.x+=(70*3)
            move[1]=42
        elif(move[1]==28): # at 28
            goti.y-=(70*6)
            goti.x-=(70*4)
            move[1]=84
        elif(move[1]==51): # at 51
            goti.y-=(70*1)
            goti.x-=(70*3)
            move[0]=1
            move[1]=67
        elif(move[1]==80): # at 80
            goti.y-=(70*2)
            goti.x+=(70*0)
            move[1]=100
        elif(move[1]==71): # at 71
            goti.y-=(70*2)
            goti.x+=(70*0)
            move[1]=91

def check_snakes(goti,move):
    if(move[1]<100):
        if(move[1]==17):   # at 17
            goti.y+=(70*1)
            goti.x+=(70*3)
            move[0]=1
            move[1]=7
        elif(move[1]==54): # at 54
            goti.y+=(70*2)
            goti.x+=(70*0)
            move[1]=34
        elif(move[1]==62): # at 62
            goti.y+=(70*5)
            goti.x+=(70*0)
            move[0]=-1
            move[1]=19
        elif(move[1]==64): # at 64
            goti.y+=(70*1)
            goti.x-=(70*3)
            move[1]=60
            move[0]=-1
        elif(move[1]==87): # at 87
            goti.y+=(70*6)
            goti.x-=(70*3)
            move[1]=24
        elif(move[1]==93): # at 93
            goti.y+=(70*2)
            goti.x-=(70*0)
            move[1]=73
        elif(move[1]==95): # at 95
            goti.y+=(70*2)
            goti.x+=(70*0)
            move[1]=75
        elif(move[1]==98): # at 98
            goti.y+=(70*2)
            goti.x-=(70*1)
            move[1]=79
winner=[]

wins=["BLUE","GREEN","RED","YELLOW"]

def main():

    num=int(input("Number of players (1 to 4): "))
    print("Press Space to play for each player one by one")
    
    clock.tick(0)

    for i in range(num):
        gotis.append(pygame.Rect(-60,640,50,50))
        move.append([1,0,1])
        
    running = True
    turn=0
    GAME.fill(BG)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if(len(gotis)>0):
                        pos=turn%len(gotis)
                        if(move_goti(gotis[pos],move[pos])==1):
                            winner.append(wins[pos])
                            gotis.remove(gotis[pos])
                            move.remove(move[pos])
                            wins.remove(wins[pos])
                            GOTIS.remove(GOTIS[pos])
                        turn+=1 
                    else:
                        running=False
                        break                    
            if event.type == pygame.QUIT:
                running=False

        keypress = pygame.key.get_pressed()
        draw()  
    print("The winners are: ")
    for i in winner:
        print(i)
    pygame.quit()

main()