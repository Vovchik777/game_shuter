import pygame

class Events:
    running = True

    def process(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False