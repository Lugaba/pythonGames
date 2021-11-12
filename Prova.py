import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
SCREEN_SIZE = (800,600)
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((255,255,255))

contadorCor = 0
cores = [(0, 0, 255), (0,0,0), (255,0,0), (255,255,0), (0,255,0)]


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        print(event)


    if contadorCor >= len(cores):
        contadorCor = 0

    pygame.draw.rect(screen, cores[contadorCor], (750, 570, 50, 30), 0)

    # Random está menor que largura e altura para aparecer apenas dentro da tela
    pygame.draw.rect(screen, cores[contadorCor], (randint(0, 750), randint(0, 570), 50, 30), 0)
    pygame.display.update()
    pygame.time.delay(1000)
    contadorCor += 1