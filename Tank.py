import pygame
import time
import random

pygame.init()

width = 1440
height = 785

gameWin = pygame.display.set_mode((width, height))
pygame.display.set_caption('ARCTAN(KS)')
clock = pygame.time.Clock()


background = pygame.image.load("tank background.jpeg")
background = pygame.transform.scale(background, (width, height))

'''def moving(): #moving backgroundnot working, covers everything else. future project
        i=0
        runing = True
        while runing:
            gameWin.fill((0,0,0))
            gameWin.blit(background,(i,0))
            gameWin.blit(background,(width+i,0))
            if (i==-width):
                gameWin.blit(background,(width+i,0))
                i=0
            i-=1
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        runing = False
            pygame.display.update()
        pygame.quit()'''



def textObjects(text, color, size="small"):
    if size == "vsmall":
        font=pygame.font.SysFont("Courier", 15)
        textSurf = font.render(text, True, color)
    if size == "small":
        font=pygame.font.Font("ARCADECLASSIC.TTF", 35)
        textSurf = font.render(text, True, color)
    if size == "medium":
        font=pygame.font.Font("ARCADECLASSIC.TTF", 45)
        textSurf = font.render(text, True, color)
    if size == "large":
        font=pygame.font.Font("ARCADE.TTF", 150)
        textSurf = font.render(text, True, color)
    return textSurf, textSurf.get_rect()

def show_message(msg, color, y_displace=0, size="small"):
    textSurf, textRect = textObjects(msg, color, size)
    textRect.center = (int(width / 2), int(height / 2) + y_displace)
    gameWin.blit(textSurf, textRect)

class Button:
#creats buttonns 
    def __init__(self, text,pos, font, bg="#F6EB14"):
        self.x, self.y = pos
        self.font = pygame.font.Font("ARCADECLASSIC.TTF", font)
        self.text=text
        self.text = self.font.render(self.text, 1, pygame.Color("#F6EB14"))
        self.change_text(bg)
 
    def change_text(self, bg="blue"):
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        
 
    def show(self):
        gameWin.blit(self.text , (self.x, self.y))
 
    def click(self, event,action):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if action == "quit":
                        pygame.quit()
                        quit()

                    if action == "controls":
                        controlsWin()

                    if action == "play":
                        mainGame()

                    if action == "main":
                        mainWindow()


def controlsWin():
    
    button1 = Button("Play", (450, 700),  font=30)

    button2 = Button("Main", (650, 700), font=30)

    button3 = Button("Quit", (850, 700), font=30)
    

    while True:
        '''gameWin.fill('#000000')''' #if we want background color black
        gameWin.blit(background,(0,0))
        Green = (0, 255, 0)
        show_message("ARCTAN(KS)", '#FF9526', -200, size="large")
        show_message("Instructions", '#EF4423', -100, size="medium")
        show_message("Enter  functions  to  determine  the  trajectory  of  your  missile", '#4FAF44', -30)
        show_message("Use  the  correct  function  to  avoid  the  obstacles", '#4FAF44', 30)
        show_message("and  obliterate  the  enemy  tank!", '#4FAF44', 90)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event,'play')
            button2.click(event,'main')
            button3.click(event,'quit')
        button1.show()
        button2.show()
        button3.show()
    
        clock.tick(30)
        pygame.display.update()




def mainWindow ():
    button1 = Button("Play", (680, 530),  font=30)

    button2 = Button("Controls", (650, 610), font=30)

    button3 = Button("Quit", (680, 690), font=30)
    

    while True:
        '''gameWin.fill('#000000')''' #if we want home page background vintage yellow
        gameWin.blit(background,(0,0))
        Green = (0, 255, 0)
        show_message("ARCTAN(KS)", '#FF9526', -150, size="large")
        show_message("Welcome to the game!", '#A4FC52',-30, size="medium")
        show_message("Choose any of the following to move forward", '#A4FC52', 50, size="medium")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event,'play')
            button2.click(event,'controls')
            button3.click(event,'quit')
        button1.show()
        button2.show()
        button3.show()
    
        clock.tick(30)
        pygame.display.update()


mainWindow()
