import random
import time

import pygame
import events
from events import Events
from colors import *
from config import *
from config_spaceship import *

shipX = 20
shipY = 10
speed = 10

bulletX = shipX + 34
bulletY = shipY / 2
bulletspeed = 20

pygame.init()

event = Events()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("шутер")
clock = pygame.time.Clock()

background_image = pygame.image.load('images/fon.jpg')
spaceship_image = pygame.image.load('images/spaceship.png')
bullet_image = pygame.image.load('images/pula2.png')
asteroid_image = pygame.image.load('images/asteroid.png')
running = True

# class Bullets(pygame.sprite.Sprite):
#     pass


bullets = []#pygame.sprite.Group()


asteroidspeed = 50

def asteroid():
    global HEIGHT,asteroid_image,screen,asteroidspeed
    coordY=random.randint(0,HEIGHT)
    coordX = WIDTH
    screen.blit(asteroid_image,(coordX-100,coordY))
    coordX-=asteroidspeed

def shot(image, x, y):
    global bullets
    bullet = [image, x, y]
    bullets.append(bullet)

t = time.time()
while running:  # event.running:

    pygame.display.flip()
    # event.process()
    screen.blit(background_image, (0, 0))
    screen.blit(spaceship_image, (shipX, shipY))
    clock.tick(FPS)


    for b in bullets:
        b[1]+=bulletspeed
        screen.blit(b[0],(b[1],b[2]))
    bullets = list(filter(lambda a: a[1]   < WIDTH,bullets))

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
        shot(bullet_image,shipX+60,shipY+16)
    if time.time() - t >= 4.0:
        t = time.time()
        asteroid()

        # screen.blit(bullet_image,(bulletX,bulletY))
        # bulletX+=bulletspeed
    # elif event.type == pygame.KEY:
    #     if event.key == pygame.K_s:
    #         shipY += speed
