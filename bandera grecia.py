# i hate my potatooooooooooOoOOOOOOOooOOOOoOoooOoooOoOo

import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 594))

# colores hermosos ÙwÚ

WHI = (255, 255, 255)
BLU = (0, 0, 255)

ventana.fill(BLU)

surface1 = pygame.Surface((800, 66))
surface1.fill(WHI)
surface2 = pygame.Surface((330, 330))
surface2.fill(BLU)

linhor = pygame.Surface((330, 66))
linhor.fill(WHI)
linver = pygame.Surface((66, 330))
linver.fill(WHI)



ventana.blit(surface1, (0, 66))
ventana.blit(surface1, (0, 198))
ventana.blit(surface1, (0, 330))
ventana.blit(surface1, (0, 462))
ventana.blit(surface2, (0, 0))
ventana.blit(linhor, (0, 132))
ventana.blit(linver, (132, 0))



# FREAKING UNBELIVABLE!!!!!
pygame.display.flip()
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break