import pygame, sys
import math

pygame.init()

win = pygame.display.set_mode((1000, 500))

pygame.display.set_caption("First Game")


#coordinates of character
x = 300
y = 200

original_ball_x = x + 20
original_ball_y = y + 12

ball_x = x + 20
ball_y = y + 12
#width and height of character
width = 50
height = 50
vel = 2

xval = 0
x_dos = ball_x
y_dos = ball_y

y_cos = ball_y + 60

tan_right_bound = x + 100;
tan_upper_bound = 0

pygame.display.set_caption("Space Invade")
icon = pygame.image.load('tank.png')
pygame.display.set_icon(icon)

image_size = (35, 35)
enemy_size = (55, 50)

#Player
playerImg = pygame.image.load("tank.png")
playerImg = pygame.transform.scale(playerImg, image_size)

#Enemy
enemyImg = pygame.image.load("enemy.png")
enemyImg= pygame.transform.scale(enemyImg, enemy_size)
enemyX = 800
enemyY = 200
enemyX_change = 0

base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(0,0,1000, 32)
color = pygame.Color('lightskyblue3')

user_text = ""

def player(x, y):
    win.blit(playerImg, (x, y))

def enemy(x, y):
    win.blit(enemyImg, (x,y))

def isCollision(enemyX, enemyY, ball_x, ball_y):
    distance = math.sqrt((math.pow(((enemyX)-ball_x),2)) + (math.pow(((enemyY+30)-ball_y), 2)))
    if distance < 10:
        return True
    else:
        return False

poly_x = 1
poly_y = 200

run = True
#loop to run the game

#PROJECTILE

active = True
delay = 0
while run:
    pygame.time.delay(delay)

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

    if active == False:
        for num in user_text:
            if num.isdigit():
                xval += 1
                ball_x = x_dos + xval * 5
                ball_y = poly_y - pow(xval, int(num))
                print(str(ball_x))
                delay = 100

        if user_text == "sin(x)":
            if (collision != True):
                ball_x = x_dos + xval* 50
                xval += .1
                ball_y = y_dos - (math.sin(xval) * 50)
                delay = 30
        elif user_text == "cos(x)":
            if (collision != True):
                ball_x = x_dos + xval* 50
                xval += .1
                ball_y = y_cos - (math.cos(xval) * 50)
                delay = 30
        elif user_text == "tan(x)":
            if (collision != True and (ball_y >= tan_upper_bound)):
                ball_x = x_dos + xval* 50
                xval += .1
                ball_y = y_dos - (math.tan(xval) * 50)
                delay = 100
        elif ball_x == original_ball_x:
            active = True

    collision = isCollision(enemyX, enemyY, ball_x, ball_y)


    if (collision != True and (ball_y <=  0 or ball_x >= 1000)):
       win.fill((0,0,0))
       ball_x = original_ball_x
       ball_y = original_ball_y

       poly_x = 1

       xval = 0
       active = True

    elif active == True:
        win.fill((0,0,0))

    pygame.draw.rect(win, color, input_rect, 2)

    text_surface = base_font.render(user_text, True, (255, 255, 255))
    win.blit(text_surface, (input_rect.x,input_rect.y+5))

    pygame.draw.circle(win, (255, 0, 0), (ball_x, ball_y), 5)
    player(x, y)
    enemy(enemyX, enemyY)
    pygame.display.update()

    if collision == True:
        break

pygame.quit()
