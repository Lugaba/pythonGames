import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()
SCREEN_SIZE = (800,600)
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((255,255,255))


azul = (0, 0, 255)
preto = (0,0,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
verde = (0,255,0)

rodada = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        print(event)

    posicaoX = random.randint(0, 800)
    posicaoY = random.randint(0, 600)

    if rodada == 0:
        pygame.draw.rect(screen, azul, (posicaoX, posicaoY, 100, 100), 0)
    elif rodada == 1:
        pygame.draw.rect(screen, preto, (posicaoX, posicaoY, 100, 100), 0)
    elif rodada == 2:
        pygame.draw.rect(screen, vermelho, (posicaoX, posicaoY, 100, 100), 0)
    elif rodada == 3:
        pygame.draw.rect(screen, amarelo, (posicaoX, posicaoY, 100, 100), 0)
    elif rodada == 4:
        pygame.draw.rect(screen, verde, (posicaoX, posicaoY, 100, 100), 0)
    else:
        rodada = 0
    rodada += 1

    pygame.display.update()
    pygame.time.delay(1000)
