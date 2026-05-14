#crear una mafufada usando los elementos gráficos vistos con mi papa de la fortuna, es decir: si, hacelo

import pygame
import sys
import math
import random
import time

pygame.init()

ventana = pygame.display.set_mode((600, 600))


#colores mafufos:
# ----------------------------------------------------------------------------------------
RED = (255, 0, 0)
GRE = (0, 255, 0)
BLU = (0, 0, 255)
WHI = (255, 255, 255)
rancol = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
rosado = (237, 138, 237)
orange = (255, 165, 0)
yellow = (255, 255, 0)
brown = (188, 150, 120)
cielo = (0, 200, 200)
metal = (191, 191, 191)
# ----------------------------------------------------------------------------------------
ventana.fill(cielo)
piso = pygame.image.load("assets/images/piso.png")
ventana.blit(piso, (0, 500))

pygame.draw.rect(ventana, WHI, (275, 150, 50, 50), 5)
pygame.draw.rect(ventana, WHI, (275, 450, 50, 50), 5)
pygame.draw.rect(ventana, WHI, (125, 300, 50, 50), 5)
pygame.draw.rect(ventana, WHI, (425, 300, 50, 50), 5)

pygame.draw.line(ventana, metal, (70, 530), (300, 300), 30)
pygame.draw.line(ventana, metal, (300, 300), (530, 530), 30)


pygame.draw.circle(ventana, RED, (300, 300), 150, 5)


pygame.draw.line(ventana, RED, (300, 150), (300, 450), 5)
pygame.draw.line(ventana, RED, (150, 300), (450, 300), 5)

pygame.draw.arc(ventana, rancol, (500, 500, 50, 50), math.pi/4, 7*math.pi/4, 100)
pygame.draw.arc(ventana, rancol, (50, 500, 50, 50), math.pi/4, 7*math.pi/4, 100)
pygame.draw.arc(ventana, rancol, (200, 500, 50, 50), math.pi/4, 7*math.pi/4, 100)


fuente = pygame.font.SysFont("Arial", 35, 1, 1)
texto = fuente.render("Rolando Parra", 1, WHI)
ventana.blit(texto, (50, 50))












pygame.display.flip()

while True:
    time.sleep(0.5)
    rancol = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()