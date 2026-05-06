import random
import pygame
pygame.init()

pantalla = pygame.display.set_mode((800, 600))

player = pygame.image.load('images/75cee04c0ed692fd3411060c85fa2ab8.jpg')

x = 400
y = 300

rancol = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    pantalla.fill(rancol)
    pantalla.blit(player, (x, y))
    pygame.display.flip()