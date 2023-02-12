import pygame, sys
import tkinter as tk
import math


count = 1
root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
BLUE = (65, 105, 225)

WINDOW_HEIGHT = height
WINDOW_WIDTH = width

class level:
    def __init__(self,allyTank,enemyTank,increment,obstacles):
        self.allyTank = allyTank
        self.enemyTank = enemyTank
        self.increment = increment
        self.obstacles = obstacles


level1 = level([0,0],[1, 3],1,[[0,10,1,9.5],[-5,10,1,9.5]])
level2 = level([-1,1],[2,1],1,[[0,10,1,9.5]])


def main():
    global SCREEN, CLOCK, font_color, font_obj, playerImg, enemyImg, blockSize
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(BLACK)
    pygame.display.set_caption('ArcTan(ks)')

    font_color=(0,150,250)
    font_obj=pygame.font.Font("coure.fon",25)
    blockSize = round(float((WINDOW_HEIGHT/20)))



    icon = pygame.image.load('tank.png')
    pygame.display.set_icon(icon)

    image_size = (40, 40)
    enemy_size = (50, 50)

    #Player
    playerImg = pygame.image.load("tank.png")
    playerImg = pygame.transform.scale(playerImg, image_size)

    #Enemy
    enemyImg = pygame.image.load("enemy.png")
    enemyImg= pygame.transform.scale(enemyImg, enemy_size)



    while True:

        fight(eval("level"+str(count)).allyTank,eval("level"+str(count)).enemyTank,eval("level"+str(count)).increment,eval("level"+str(count)).obstacles)

        pygame.display.update()

def drawGrid(increment):
    for x in range(round(float(WINDOW_WIDTH*(7/16))), WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, GREEN, rect, 1)


    count = 0
    for a in range(20+1):
        text_obj=font_obj.render(str(round(float((count-10)*increment),2)),True,font_color)
        SCREEN.blit(text_obj,(WINDOW_WIDTH*(7/16)+(count*blockSize-blockSize*3/8),WINDOW_HEIGHT/2))
        count += 1

    count = 0
    for b in range(20+1):
        text_obj=font_obj.render(str(-(round(float((count-10)*increment),2))),True,font_color)
        SCREEN.blit(text_obj,(WINDOW_WIDTH*(11/16)+blockSize *3/4,(count*blockSize)))
        count += 1

def fight(allyTank,enemyTank,increment,obstacles):

    #coordinates of character
    x = (WINDOW_WIDTH*(23/32))+(allyTank[0]*blockSize)-20
    y = (WINDOW_HEIGHT/2)-(allyTank[1]*blockSize)-20

    original_ball_x = x + 20
    original_ball_y = y + 12

    ball_x = x + 20
    ball_y = y + 12
    #width and height of character
    vel = 2

    xval = 0
    x_dos = ball_x
    y_dos = ball_y

    y_cos = ball_y + 60

    tan_right_bound = x + 100;

    pygame.display.set_caption("Space Invade")

    enemyX = (WINDOW_WIDTH*(23/32))+(enemyTank[0]*blockSize)-25
    enemyY = (WINDOW_HEIGHT/2)-(enemyTank[1]*blockSize) -25
    enemyX_change = 0

    base_font = pygame.font.Font(None, 32)
    user_text = ''

    input_rect = pygame.Rect(0,0,800, 32)
    color = pygame.Color('lightskyblue3')

    user_input = ""

    def player(x, y):
        SCREEN.blit(playerImg, (x,y))
    def enemy(x, y):
        SCREEN.blit(enemyImg, (x,y))


    def isCollision(enemyX, enemyY, ball_x, ball_y):
        distance = math.sqrt((math.pow(((enemyX)-ball_x),2)) + (math.pow(((enemyY+30)-ball_y), 2)))
        if distance < blockSize:
            return True
        else:
            return False



    run = True

    entered_input = False

    active = True

    while run:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if active == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[0:-1]
                    elif event.key == pygame.K_RETURN:
                        active = False
                    else:
                        user_text += event.unicode

        collision = isCollision(enemyX, enemyY, ball_x, ball_y)

        if user_text == "sin(x)" and active == False:
            if (collision != True ):
                ball_x = x_dos + xval* 50
                xval += .1
                ball_y = y_dos - (math.sin(xval) * 50)
        elif user_text == "cos(x)" and active == False:
            if (collision != True):
                ball_x = x_dos + xval* 50
                xval += .1
                ball_y = y_cos - (math.cos(xval) * 50)
        elif user_text == "tan(x)" and active == False:
            if (collision != True and (ball_x < tan_right_bound)):
                ball_x = x_dos + xval* 50
                xval += .1
                ball_y = y_dos - (math.tan(xval) * 50)
        else:
            active = True


        if (collision != True and (ball_y <=  0 or ball_x >= width)):
            count = 1
            SCREEN.fill((0,0,0))
            drawGrid(eval("level"+str(count)).increment)
            ball_x = original_ball_x
            ball_y = original_ball_y
            poly_x = 1

            xval = 0
            active = True
        elif (collision == True):
            count += 1
            if count == 3:
                pygame.quit()
            fight(eval("level"+str(count)).allyTank,eval("level"+str(count)).enemyTank,eval("level"+str(count)).increment,eval("level"+str(count)).obstacles)
        elif active == True:
            count = 1
            SCREEN.fill((0,0,0))
            drawGrid(eval("level"+str(count)).increment)


        pygame.draw.rect(SCREEN, color, input_rect, 2)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        SCREEN.blit(text_surface, (input_rect.x,input_rect.y+5))

        pygame.draw.circle(SCREEN, (255, 0, 0), (ball_x, ball_y), 5)

        for i in obstacles:
            pygame.draw.rect(SCREEN, BLUE, pygame.Rect((WINDOW_WIDTH*(23/32)-i[2]*blockSize/2)+(i[0]*blockSize),(WINDOW_HEIGHT/2)-(i[1]*blockSize),i[2]*blockSize,i[3]*blockSize),2,3)

        player(x, y)
        enemy(enemyX, enemyY)
        pygame.display.update()



main()
