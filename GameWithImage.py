import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((850, 529))
pygame.display.set_caption("CENÁRIO")
JogoAtivo = True
imagem = "images/cenario.png"
background = pygame.image.load(imagem)
while JogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False
    screen.blit(background,(0,0))
    pygame.display.update()
pygame.time.delay(2000)
pygame.quit()