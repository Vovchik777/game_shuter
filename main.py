
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

pygame.display.flip()


while event.running:
    event.process()

