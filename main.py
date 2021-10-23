import pygame
from pygame.locals import *

#initializing pygame
pygame.init()

#set up window resolution
screen_width = 1280
screen_height = 720
screen_resolution = (screen_width,screen_height)

screen = pygame.display.set_mode(screen_resolution)
pygame.display.set_caption("Super Start Jumper")


#Keep the game running
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

