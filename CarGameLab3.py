# Autor: Felipe Torales Leite e Luca Amelio Hummel
# Tia: 32034539 e 32016816

import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((772, 444))
pygame.display.set_caption("CENÁRIO")
JogoAtivo = True

fundo = "images/fundoLab3.png"
carroImage = "images/ferrari1.png"
carroImageInvertida = "images/ferrari1Invertida.png"
background = pygame.image.load(fundo)
carro = pygame.image.load(carroImage)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

my_font = pygame.font.SysFont("arial", 40, bold=True, italic=False)
textoGameOver = my_font.render("Game Over", True, red, white)

posY = 60
posX = 0
while JogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False
        if evento.type == KEYDOWN:
            if evento.key == K_RIGHT and (posY == 60 or posY == 340):
                posX += 100
            elif evento.key == K_LEFT and posY == 200:
                posX -= 100

    screen.blit(background, (0, 0))

    if posY == 60 and posX > 772:
        posY = 200
        posX = 700
        carro = pygame.image.load(carroImageInvertida)
    elif posY == 200 and posX < 0:
        posY = 340
        posX = 0
        carro = pygame.image.load(carroImage)
    elif posY == 340 and posX > 772:
        screen.blit(textoGameOver, (386, 222))
        JogoAtivo = False

    screen.blit(carro, (posX, posY))
    pygame.display.update()
    
pygame.time.delay(2000)
pygame.quit()