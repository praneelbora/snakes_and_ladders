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

GOTI_B = pygame.image.load("Assets/goti_blue.png")
GOTI_B = pygame.transform.scale(GOTI_B,(50,50))
GOTI_G = pygame.image.load("Assets/goti_green.png")
GOTI_G = pygame.transform.scale(GOTI_G,(50,50))
GOTI_R = pygame.image.load("Assets/goti_red.png")
GOTI_R = pygame.transform.scale(GOTI_R,(50,50))
GOTI_Y = pygame.image.load("Assets/goti_yellow.png")
GOTI_Y = pygame.transform.scale(GOTI_Y,(50,50))
GOTIS=[GOTI_B,GOTI_G,GOTI_R,GOTI_Y]
def draw(gotis):
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
    


def rand():
    val=random.random()*6
    return int(val)

def main():
    move=[[1,0,1],[1,0,1]]
    # move[][0] helps in adding or subtracting values of goti.x
    # move[][1] helps stopping goti at 100 position
    # move[][2] says how many steps to be taken by that goti
    running = True
    clock = pygame.time.Clock()
    GAME.fill(BG)
    goti_b=pygame.Rect(-60,640,50,50)
    goti_g=pygame.Rect(-60,640,50,50)
    gotis=[goti_b,goti_g]
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        keypress = pygame.key.get_pressed()
        move_goti(goti_b,move,0)
        move_goti(goti_g,move,1)
        draw(gotis)  
    pygame.quit()

main()