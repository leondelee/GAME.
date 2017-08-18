import sys,random,pygame,time
from pygame.locals import *
pygame.init()
red=[255,0,0]
white=[255,255,255]
black=[0,0,0]
screen = pygame.display.set_mode((640, 480))
global scoreint
scoreint=0
game_over="GAME OVER!"
start="Start"
modeeasy="Easy"
modehard="Hard"

fonto=pygame.font.SysFont("arial",50)
test1=fonto.render(game_over,True,white)
fonts=pygame.font.SysFont("arial",35)
fontl=pygame.font.SysFont("arial",30)
test2=fonts.render(start,True,black)
test3=fonts.render(modeeasy,True,black)
test4=fonts.render(modehard,True,black)
test5=fontl.render("Click to continue...",True,white)
dead=False
flag1=0
pygame.display.set_caption('Leon 贪吃蛇')
def mid():
    screen = pygame.display.set_mode((640, 480))
    while not pygame.mouse.get_pressed()[0]:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            pygame.draw.rect(screen, white, (120, 215, 100, 50))
            pygame.draw.rect(screen, white, (420, 215, 100, 50))
            screen.blit(test3,(130,225))
            screen.blit(test4,(430,225))
        pygame.display.flip()
    if 120<pygame.mouse.get_pos()[0]<220 and  215<pygame.mouse.get_pos()[1]<265:
        play_easy()
    elif 420<pygame.mouse.get_pos()[0]<520 and 215<pygame.mouse.get_pos()[1]<265:
        play_hard()
    else:
        mid()

def death():
    while not pygame.mouse.get_pressed()[0]:
        screen=pygame.display.set_mode((640,480))
        screen.blit(test1,(70,215))
        screen.blit(test5,(70,400))
        pygame.display.flip()
    start()
def start():
    pygame.init()
    screen=pygame.display.set_mode((640,480))
    while  not 270 < pygame.mouse.get_pos()[0] < 370 or not 215 < pygame.mouse.get_pos()[1] < 265 or not pygame.mouse.get_pressed()[0]:
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            pygame.draw.rect(screen,white,(270,215,100,50))
            screen.blit(test2,(280,225))

        pygame.display.flip()
    mid()
def play_easy():
    wc=0
    flag1=0
    flag2=0
    wc1=0
    scoreint=0
    flag=1
    pygame.init()
    screen=pygame.display.set_mode((640,480))
    position = [400,200]
    apple_position = [300,300]
    snake_seg = [position, [position[0] - 20, position[1]], [position[0] - 40, position[1]]]
    direction = 4
    changedirection = 4
    fpsClock = pygame.time.Clock()
    dead=False
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_UP or event.key==K_w:
                    changedirection=8
                elif event.key==K_DOWN or event.key==K_s:
                    changedirection=5
                elif event.key==K_LEFT or event.key==K_a:
                    changedirection=4
                elif event.key==K_RIGHT or event.key==K_d:
                    changedirection=6
        if changedirection==8 and direction!=5:
            direction=8
        elif changedirection==5 and direction!=8:
            direction=5
        elif changedirection==4 and direction!=6:
            direction=4
        elif changedirection==6 and direction!=4:
            direction=6
        if position[0]==0 and flag1==0:
            position[0]=640
        elif position[0]==640:
            position[0]=-20
            wc+=1
            flag1=1
        elif position[1]==0 and flag2==0 :
            position[1]=480
        elif position[1]==480:
            position[1]-=500
            flag2=1
            wc1+=1
        if wc!=0:
            wc+=1
        if wc1!=0:
            wc1+=1
        if direction==8:
            position[1]-=20
        elif direction==5:
            position[1]+=20
        elif direction==4:
            position[0]-=20
        elif direction==6:
            position[0]+=20
        snake_seg.insert(0,list(position))
        if snake_seg[0][0]==apple_position[0] and snake_seg[0][1]==apple_position[1]:
            flag=0
        else:
            snake_seg.pop()
        if flag==0:
            apple_x = random.randint(1, 32)
            apple_y = random.randint(1, 24)
            apple_position = [apple_x * 20, apple_y * 20]
            scoreint+=5
            flag=1
        score = ("Scores:%d" % scoreint)
        test5 = fonts.render(score, True, white)
        time.sleep(100 / 1000)
        screen.fill(black)
        for i in snake_seg:
            pygame.draw.rect(screen,white,(i[0],i[1],20,20))
            pygame.draw.rect(screen,red,(apple_position[0],apple_position[1],20,20))
        screen.blit(test5,(5,5))
        pygame.display.flip()
        for i in range(1,len(snake_seg)):
            if direction==8:
                if snake_seg[0][0]==snake_seg[i][0] and snake_seg[0][1]==snake_seg[i][1]+20:
                    dead=True
            elif direction==4:
                if snake_seg[0][0]==snake_seg[i][0]+20 and snake_seg[0][1]==snake_seg[i][1]:
                    dead=True
            elif direction==5:
                if snake_seg[0][0]==snake_seg[i][0] and snake_seg[0][1]==snake_seg[i][1]:
                    dead=True
            elif direction==6:
                if snake_seg[0][0]==snake_seg[i][0] and snake_seg[0][1]==snake_seg[i][1]:
                    dead=True
        if dead:
            death()
        fpsClock.tick(5)
        if wc>=3:
            flag1=0
            wc=0
        if wc1>=3:
            flag2=0
            wc=0
def play_hard():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    position = [400, 200]
    apple_position = [300, 300]
    snake_seg = [position, [position[0] - 20, position[1]], [position[0] - 40, position[1]]]
    direction = 4
    changedirection = 4
    fpsClock = pygame.time.Clock()
    dead=False
    flag=1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    changedirection = 8
                elif event.key == K_DOWN or event.key == K_s:
                    changedirection = 5
                elif event.key == K_LEFT or event.key == K_a:
                    changedirection = 4
                elif event.key == K_RIGHT or event.key == K_d:
                    changedirection = 6
        if changedirection == 8 and direction != 5:
            direction = 8
        elif changedirection == 5 and direction != 8:
            direction = 5
        elif changedirection == 4 and direction != 6:
            direction = 4
        elif changedirection == 6 and direction != 4:
            direction = 6
        if direction == 8:
            position[1] -= 20
        elif direction == 5:
            position[1] += 20
        elif direction == 4:
            position[0] -= 20
        elif direction == 6:
            position[0] += 20
        snake_seg.insert(0, list(position))
        if snake_seg[0][0] == apple_position[0] and snake_seg[0][1] == apple_position[1]:
            flag = 0
        else:
            snake_seg.pop()
        if flag == 0:
            apple_x = random.randint(1, 32)
            apple_y = random.randint(1, 24)
            apple_position = [apple_x * 20, apple_y * 20]
            flag=1
        screen.fill(black)
        pygame.draw.line(screen,white,(0,0),(635,0),5)
        pygame.draw.line(screen, white, (635, 0), (635, 476), 5)
        pygame.draw.line(screen, white, (635, 476), (0, 476), 5)
        pygame.draw.line(screen, white, (0, 476), (0, 0), 5)
        for i in snake_seg:
            pygame.draw.rect(screen, white, (i[0], i[1], 20, 20))
            pygame.draw.rect(screen, red, (apple_position[0], apple_position[1], 20, 20))
        if len(snake_seg) <= 10:
            fpsClock.tick(5)
        elif 10 < len(snake_seg) <= 20:
            fpsClock.tick(10)
        else:
            fpsClock.tick(15)
        for i in range(1,len(snake_seg)):
            if direction==8:
                if snake_seg[0][0]==snake_seg[i][0] and snake_seg[0][1]==snake_seg[i][1]+20:
                    dead=True
            elif direction==4:
                if snake_seg[0][0]==snake_seg[i][0]+20 and snake_seg[0][1]==snake_seg[i][1]:
                    dead=True
            elif direction==5:
                if snake_seg[0][0]==snake_seg[i][0] and snake_seg[0][1]==snake_seg[i][1]:
                    dead=True
            elif direction==6:
                if snake_seg[0][0]==snake_seg[i][0] and snake_seg[0][1]==snake_seg[i][1]:
                    dead=True
        if direction==8:
            if snake_seg[0][1]==0:
                dead=True
        elif direction==4:
            if snake_seg[0][0]==0:
                dead=True
        elif direction==5:
            if snake_seg[0][1]==480:
                dead=True
        elif direction==6:
            if snake_seg[0][0]==640:
                dead=True
        if dead:
            death()
        fpsClock.tick(10)
        pygame.display.flip()
start()




