import pygame
from time import sleep
import random

pygame.init()

display_width = 800
display_height = 600
car_width = 73

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
red_dark = (200, 0, 0)
green = (0, 255, 0)
green_dark = (0, 200, 0)

carImg = pygame.image.load('racecar.png')
carImg2 = pygame.image.load('racecar2.png')

paused = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Race_Example')
pygame.display.set_icon(carImg2)


clock = pygame.time.Clock()

def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: " + str(int(count)), True, black)
    gameDisplay.blit(text, (0,0))
5
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("comicsansms", 60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    

def crash():
    largeText = pygame.font.SysFont("comicsansms", 60)
    TextSurf, TextRect = text_objects("YOU CRASHED!", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        button("RESTART", 150, 450, 130, 50, green_dark, green, game_loop)
        button("QUIT", 550, 450, 100, 50, red_dark, red, quit_game)
        pygame.display.update()
        clock.tick(15)

def quit_game():
    pygame.quit()
    quit()

def unpause():
    global paused
    paused = False

def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 60)
        TextSurf, TextRect = text_objects("Dodgey", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!", 150, 450, 100, 50, green_dark, green, game_loop)
        button("QUIT!", 550, 450, 100, 50, red_dark, red, quit_game)
        
        pygame.display.update()
        clock.tick(15)
        
def pause():

    largeText = pygame.font.SysFont("comicsansms", 60)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)

        
        button("Continue", 150, 450, 100, 50, green_dark, green, unpause)
        button("QUIT!", 550, 450, 100, 50, red_dark, red, quit_game)
        
        pygame.display.update()
        clock.tick(15)
    
        

def game_loop():
    global paused

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, (display_width - 100))
    thing_starty = -600
    thing_speed = 12
    thing_width = 100
    thing_height = 100
    dodged = 0

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_p:
                    paused = True
                    pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            

            
        gameDisplay.fill(white)
        x += x_change
        things(thing_startx, thing_starty, thing_width, thing_height, red)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, (display_width - thing_width))
            dodged += 1

        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()
                
        pygame.display.update()
        clock.tick(30)
    
game_intro()

