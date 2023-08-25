import pygame

import config_spaceship
from config_spaceship import *
class Events:
    running = True

    def process(self):
        global shipY
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_s:
                    shipY+=speed
                    