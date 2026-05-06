# importamos la libreria pygame
import pygame
import sys
import random

# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# establecer titulo de la ventana
pygame.display.set_caption("Rebotes rectángulo")

# definición colores
rojo = (255,0,0)
azul = (0,0,255)
rancol = (0, 0, 0)

# variable de movimiento
XX = 300
YY = 300
MOVIMIENTO = 9

# Objeto para la gestión del tiempo
clock = pygame.time.Clock()


# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    rancol = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # movimiento del rectángulo
    XX = random.randint(10, 320) + MOVIMIENTO
    YY = random.randint(10, 320) + MOVIMIENTO
    # esto cambia la dirección, haciendo que rebote :3
    if XX >= 320:
        XX = 320
        MOVIMIENTO = -9
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 9

    if XX >= 320:
        XX = 320
        MOVIMIENTO = -9
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 9

    # dibujar rectangulo en ventana
    pygame.draw.rect(ventana, rancol, (XX, YY, 80, 80))
    pygame.draw.rect(ventana, rancol, (XX, YY, 80, 80))
    pygame.draw.rect(ventana, rancol, (XX, YY, 80, 80))
    pygame.draw.rect(ventana, rancol, (XX, YY, 80, 80))
    pygame.draw.rect(ventana, rancol, (XX, YY, 80, 80))

    # actualizar visualización de la ventana
    pygame.display.flip()
