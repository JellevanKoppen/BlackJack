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


gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(black)

def intro():
    intro = true
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
