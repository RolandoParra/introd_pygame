import pygame
pygame.init()
ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("The Freaking Unbelievable Game")

# my colores ÙwÚ
blu = (0, 0, 255)
red = (255, 0, 0)
gre = (0, 255, 0)
wai = (255, 255, 255)
bla = (0, 0, 0)
yel = (255, 255, 0)
pur = (170, 0, 255)



ventana.fill(wai)

l1 = pygame.Surface((10, 400))
l1.fill(bla)
l2 = pygame.Surface((400, 10))
l2.fill(bla)

f1 = pygame.Surface((50, 50))
f1.fill(red)
f2 = pygame.Surface((50, 50))
f2.fill(gre)
f3 = pygame.Surface((50, 50))
f3.fill(blu)
f4 = pygame.Surface((50, 50))
f4.fill(yel)
f5 = pygame.Surface((50, 50))
f5.fill(pur)

ventana.blits([(l1, (195, 0)), (l2, (0, 195)), (f1, (50, 50)), (f2, (300, 50)), (f3, (50, 300)), (f4, (300, 300)), (f5, (175, 175))])
pygame.display.flip()

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()