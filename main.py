
import pygame,random

import events
from events import Events
from colors import *
from config import *

pygame.init()

event = Events()

screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("шутер")
clock = pygame.time.Clock()

background_image = pygame.image.load('images/fon.jpg')


while event.running:
    event.process()
    screen.blit(background_image,(0,0))
    pygame.display.flip()
