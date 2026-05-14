import pygame
import random

mario = pygame.image.load("assets/images/mario03.png")
arbol = pygame.image.load("assets/images/arbol.png")
escudo = pygame.image.load("assets/images/escudoColegio.png")

pygame.init()

banana = random.randint(1, 3)

if banana == 1:
    pantalla = pygame.display.set_mode((370, 442))
    pantalla.blit(mario, (5, 5))
elif banana == 2:
    pantalla = pygame.display.set_mode((275, 200))
    pantalla.blit(arbol, (5, 5))
elif banana == 3:
    pantalla = pygame.display.set_mode((110, 143))
    pantalla.blit(escudo, (5, 5))




while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()