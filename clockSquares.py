import pygame
from random import randint


def sorteiacor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    cor = (r, g, b)
    return cor


BLACK = (0, 0, 0)
cor = sorteiacor()

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mover Caixa")

clock = pygame.time.Clock()

box_x = 300
box_y = 300
box_dir = 5
box_dirY = 5

jogoAtivo = True
while jogoAtivo:
    clock.tick(30) # taxa de frames
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False
    screen.fill(BLACK)
    box_x += box_dir
    box_y += box_dirY
    if box_x >= 620:
        box_x = 620
        box_dir = -5
        cor = sorteiacor()
    elif box_x <= 0:
        box_x = 0
        box_dir = 5
        cor = sorteiacor()
    if box_y >= 460:
        box_y = 460
        box_dirY -= 5
        cor = sorteiacor()
    elif box_y <= 0:
        box_y = 0
        box_dirY = 5
        cor = sorteiacor()

    pygame.draw.rect(screen, cor, (box_x, box_y, 20, 20))
    pygame.display.update()


pygame.time.delay(2000)
quit()
