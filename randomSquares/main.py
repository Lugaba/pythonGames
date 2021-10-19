# Autor: Felipe Torales Leite e Luca Amelio Hummel
# Tia: 32034539 e 32016816

import pygame
from Quadrado import Quadrado


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Ola Mundo")
    screen.fill((255, 255, 255))

    lado = 250

    while lado != 0:
        quadrado = Quadrado()
        quadrado.altura = lado
        quadrado.largura = lado
        quadrado.sorteiacor()
        quadrado.sorteiaX()
        quadrado.sorteiaY()

        while quadrado.posX + quadrado.largura >= 1000 or quadrado.posY + quadrado.altura >= 800:
            quadrado.sorteiaX()
            quadrado.sorteiaY()

        pygame.draw.rect(screen, quadrado.cor, (quadrado.posX, quadrado.posY, quadrado.largura, quadrado.altura), 0)
        pygame.display.flip()  # atualiza o status da tela
        pygame.time.delay(1000)
        lado = int(lado/2)

    pygame.display.flip()  # atualiza o status da tela
    pygame.time.delay(5000)
    pygame.quit()


main()
