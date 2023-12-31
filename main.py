import random
import time

import pygame
from colors import *
from config import *

shipX = 20
shipY = 10
speed = 10

asteroidudar = 0
bullets_left = 100
bulletX = shipX + 34
bulletY = shipY / 2
bulletspeed = 20

bullets_left = 100

pygame.init()

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


bullets = []  # pygame.sprite.Group()
asteroids = []

asteroidspeed = 5


def asteroid(image, x, y):
    global asteroids
    asteroid = [image, x, y]
    asteroids.append(asteroid)


def shot(image, x, y):
    global bullets,bullets_left
    bullet = [image, x, y]
    bullets.append(bullet)
    bullets_left -= 1


t = time.time()
while running:  # event.running:
    f = pygame.font.SysFont('arial', 25)
    sc_text = f.render(f'Пуль осталось: {bullets_left}', 1, RED)  # , BLUE)
    pos = sc_text.get_rect(center = (WIDTH-200,HEIGHT - 30))
    screen.blit(sc_text, pos)
    pygame.display.flip()
    # event.process()
    screen.blit(background_image, (0, 0))
    screen.blit(spaceship_image, (shipX, shipY))
    clock.tick(FPS)

    for a in asteroids:
        a[1] -= asteroidspeed
        screen.blit(a[0], (a[1], a[2]))
        if a[1] <= 0:  # WIDTH:
            asteroids = list(filter(lambda a: a[1] < 0, asteroids))
            asteroidudar += 1
            bullets_left = 100
            if asteroidudar == 3:  # len(asteroidudar) == 3:
                running = False

    # asteroids = list(filter(lambda a: a[1] < WIDTH, asteroids))
    for b in bullets:
        b[1] += bulletspeed
        screen.blit(b[0], (b[1], b[2]))
    bullets = list(filter(lambda a: a[1] < WIDTH, bullets))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
    if pygame.key.get_pressed()[pygame.K_s]:
        if shipY < HEIGHT - 34:
            shipY += speed
    elif pygame.key.get_pressed()[pygame.K_w]:
        if shipY > 0:
            shipY -= speed
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        if bullets_left > 0:
            shot(bullet_image, shipX + 60, shipY + 16)
    for a in asteroids:
        for b in bullets:
            if a[1] <= b[1] + 10 <= a[1] + 30 and a[2] <= b[2] <= a[2] + 30:
                asteroids.remove(a)
                bullets.remove(b)
                bullets_left += 7
    if time.time() - t >= 1.0:
        t = time.time()
        asteroid(asteroid_image, WIDTH, random.randint(0, HEIGHT - 30))
defeat_screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Вы проиграли!')
f = pygame.font.SysFont('arial', 24)
sc_text = f.render('Вы проиграли!', 1, RED)  # , BLUE)
pos = sc_text.get_rect(center=(600 // 2, 600 // 2))

defeat_screen.fill(BLUE)
defeat_screen.blit(sc_text, pos)
pygame.display.update()
defeat = True
while defeat:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            defeat = False
        elif event.type == pygame.KEYDOWN:
            defeat = False

        # screen.blit(bullet_image,(bulletX,bulletY))
        # bulletX+=bulletspeed
    # elif event.type == pygame.KEY:
    #     if event.key == pygame.K_s:
    #         shipY += speed
