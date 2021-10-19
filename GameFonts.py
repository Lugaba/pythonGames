import pygame
from pygame.locals import *

pygame.init()
largura = 800
altura = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('TESTE FONTE')
my_font = pygame.font.SysFont("arial", 20, bold=True, italic=False)
superficie = my_font.render("VOCÊ CLICOU AQUI", True, black, white)
JogoAtivo = True
while JogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False
    if evento.type == MOUSEBUTTONDOWN:
        x1, y1 = pygame.mouse.get_pos()
        screen.blit(superficie, (x1, y1))

    pygame.display.flip()
pygame.time.delay(2000)
quit()
