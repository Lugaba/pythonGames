import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pink Game')
screen.fill((255,0,127))
pygame.display.flip()

jogoAtivo = True
while jogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            jogoAtivo = False
        if evento.type == KEYDOWN:
            if evento.key == K_a:
                pygame.draw.line(screen, (0, 128, 0), (0, 0), (300, 300), 5)
                pygame.display.flip()
            elif evento.key == K_b:
                pygame.draw.rect(screen, (65, 105, 225), (random.randint(0, 640),
                                                          random.randint(0, 480), 20, 50), 0)
                pygame.display.flip()
            elif evento.key == K_c:
                pygame.draw.rect(screen, (255, 255, 0), (320, 240, 80, 100), 5)
                pygame.display.flip()
            elif evento.key == K_d:
                pygame.draw.circle(screen, (148, 0, 211), (100, 200), 40, 5)
                pygame.display.flip()
            elif evento.key == K_e:
                pygame.draw.ellipse(screen, (255, 255, 0), (100, 200,100, 50), 0)
                pygame.display.flip()
            elif evento.key == K_f:
                pygame.draw.polygon(screen, (148, 0, 211), ((100, 400), (10, 300),
                                                            (10, 400)), 0)
                pygame.display.flip()
pygame.time.delay(2000)
quit()
