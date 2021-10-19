import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("FERRARI")
JogoAtivo = True
fundo = "images/FundoCarro.png"
imagem = "images/ferrari1.png"
background = pygame.image.load(fundo)
carro = pygame.image.load(imagem)
X = 0
Y = 220
while JogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False
    screen.blit(background, (0, 0))
    screen.blit(carro, (X, Y))
    pygame.display.update()
    X += 10
    pygame.time.delay(50)
pygame.quit()
