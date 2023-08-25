import pygame, random

import events
from events import Events
from colors import *
from config import *
from config_spaceship import *

bullets = []

shipX = 20
shipY = 10
speed = 10

bulletX = shipX + 34
bulletY = shipY / 2
bulletspeed = 2

pygame.init()

event = Events()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("шутер")
clock = pygame.time.Clock()

background_image = pygame.image.load('images/fon.jpg')
spaceship_image = pygame.image.load('images/spaceship.png')
bullet_image = pygame.image.load('images/pula2.png')

running = True

while running:  # event.running:
    pygame.display.flip()
    # event.process()
    screen.blit(background_image, (0, 0))
    screen.blit(spaceship_image, (shipX, shipY))
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_s]:
        if shipY < HEIGHT - 34:
            shipY += speed
    elif pygame.key.get_pressed()[pygame.K_w]:
        if shipY > 0:
            shipY -= speed
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        for i in range(20):
            bullets.append({f"bullet{+i}",shipX+34, shipY/2 })
            print(bullets)
            # screen.blit(bullet_image,(bulletX,bulletY))
            # bulletX+=bulletspeed
    # elif event.type == pygame.KEY:
    #     if event.key == pygame.K_s:
    #         shipY += speed
