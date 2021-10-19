import pygame
from pygame.locals import *
import random

pygame.init()
SCREEN_SIZE = (600, 400)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Teste")
JogoAtivo = True
while JogoAtivo:
    # trata os eventos da fila de eventos
    for evento in pygame.event.get():
        print(evento)
        # verifica se o evento que veio eh para fechar a janela
        if evento.type == QUIT:
            JogoAtivo = False
        if evento.type == MOUSEBUTTONDOWN:
            x1, y1 = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255),
                                        random.randint(0, 255)), (x1, y1), 50, 0)
        if evento.type == KEYDOWN:
            print('uma tecla foi pressionada')
            if evento.key == K_ESCAPE:
                JogoAtivo = False
        if evento.type == KEYUP:
            print('uma tecla foi liberada')

    pygame.display.flip()
pygame.time.delay(2000)
pygame.quit()
