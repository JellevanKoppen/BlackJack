import pygame
from time import sleep
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
red_dark = (200, 0, 0)
green = (0, 255, 0)
green_dark = (0, 200, 0)

#BlackJackIcon = pygame.image.load('icon.png')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('BlackJack')
#pygame.display.set_icon(BlackJackIcon)
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def resolution(width, height):
    global display_width
    global display_height
    display_width = width
    display_height = height
    pygame.display.set_mode((width, height))
    print("GameDisplay Updated!")
    intro()

def button(msg,x,y,w,h,ic,ac, action=None, param1=None, param2=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None and param1 == None:
            action()
        if click[0] == 1 and action != None and param1 != None and param2 != None:
            action(param1, param2)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 60)
        TextSurf, TextRect = text_objects("Choose Resolution:", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("1080x720", (display_width*0.1), (display_height*0.8), 100, 50, green_dark, green, resolution, 1080, 720)
        button("800x600", (display_width*0.8), (display_height*0.8), 100, 50, red_dark, red, resolution, 800, 600)
        
        pygame.display.update()
        clock.tick(15)
                
        
intro()

        
