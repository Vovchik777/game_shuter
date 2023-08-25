
import pygame,random

import events
from events import Events
from colors import *
from config import *
from config_spaceship import *



pygame.init()

event = Events()

screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("шутер")
clock = pygame.time.Clock()

background_image = pygame.image.load('images/fon.jpg')
spaceship_image = pygame.image.load('images/spaceship.png')


while event.running:
    pygame.display.flip()
    event.process()
    screen.blit(background_image,(0,0))
    screen.blit(spaceship_image,(shipY,shipX))


    clock.tick(FPS)
