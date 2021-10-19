# Autor: Felipe Torales Leite e Luca Amelio Hummel
# Tia: 32034539 e 32016816

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Crescimento da árvore")

arvoreEtapa = "Slide1.png"
arvoreEtapa1 = "Slide2.png"
arvoreEtapa2 = "Slide3.png"
arvoreEtapa3 = "Slide4.png"
arvoreEtapa4 = "Slide5.png"
arvoreEtapa5 = "Slide6.png"
nuvemImage = "Nuvem.png"

background = pygame.image.load(arvoreEtapa)
nuvem = pygame.image.load(nuvemImage)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

my_font = pygame.font.SysFont("arial", 20, bold=True, italic=False)
textoCut = my_font.render("Botão esquerdo do Mouse para cortar a árvore", True, white)
textoIntru = my_font.render("Seta cima - cresce árvore || setas esquerda e direita - mexe nuvem", True, white)



posXNuvem = 0
contadorEtapa = 0
JogoAtivo = True
while JogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False
        if evento.type == KEYDOWN:
            if evento.key == K_UP:
                if contadorEtapa < 5:
                    contadorEtapa += 1
            if evento.key == K_RIGHT:
                posXNuvem += 100
            if evento.key == K_LEFT:
                posXNuvem -= 100
        if evento.type == MOUSEBUTTONDOWN:
            if contadorEtapa == 5:
                contadorEtapa = 0

    screen.blit(background, (0, 0))
    screen.blit(nuvem, (posXNuvem, 30))

    if contadorEtapa == 1:
        background = pygame.image.load(arvoreEtapa1)
    elif contadorEtapa == 2:
        background = pygame.image.load(arvoreEtapa2)
    elif contadorEtapa == 3:
        background = pygame.image.load(arvoreEtapa3)
    elif contadorEtapa == 4:
        background = pygame.image.load(arvoreEtapa4)
    elif contadorEtapa == 5:
        screen.blit(textoCut, (440, 190))
        background = pygame.image.load(arvoreEtapa5)
    else:
        screen.blit(textoIntru, (320, 190))
        background = pygame.image.load(arvoreEtapa)



    pygame.display.update()

pygame.quit()
