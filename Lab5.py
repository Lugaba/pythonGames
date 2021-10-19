# Autor: Felipe Torales Leite e Luca Amelio Hummel
# Tia: 32034539 e 32016816

import pygame, time, random


PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)

LARGURAJANELA = 500
ALTURAJANELA = 400

pygame.init()
pygame.font.init()
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('CRAAAAASH')
boomImage = pygame.image.load('images/Boom.png')

relogio = pygame.time.Clock()
ret = pygame.Rect(random.randint(0, 455), random.randint(0, 355), 45, 45)
ret2 = pygame.Rect(random.randint(0, 455), random.randint(0, 355), 45, 45)
padrao = pygame.font.get_default_font()
fonte = pygame.font.SysFont(padrao, 30)


velocidades = [2, -2]
retX = velocidades[random.randint(0,1)]
retY = velocidades[random.randint(0,1)]
ret2X = velocidades[random.randint(0,1)]
ret2Y = velocidades[random.randint(0,1)]

bateu = False

deve_continuar = True
# loop do jogo
while deve_continuar:
    # checando se ocorreu um evento QUIT
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    relogio.tick(100)
    janela.fill(PRETO)

    if ret.colliderect(ret2):
        bateu = True
        janela.blit(boomImage, (ret.x-75, ret2.y-60))
        pygame.display.flip()
        pygame.time.delay(2500)


    if bateu == False:
        if ret.x > 455 or ret.x < 0:
            retX = -retX

        if ret.y < 0 or ret.y > 355:
            retY = -retY

        if ret2.x > 455 or ret2.x < 0:
            ret2X = -ret2X

        if ret2.y < 0 or ret2.y > 355:
            ret2Y = -ret2Y

        ret.move_ip(retX, retY)
        ret2.move_ip(ret2X, ret2Y)
        pygame.draw.rect(janela, AZUL, ret)
        pygame.draw.rect(janela, AMARELO, ret2)
        pygame.display.update()
        time.sleep(0.02)
    else:
        ret = pygame.Rect(random.randint(0, 455), random.randint(0, 355), 45, 45)
        ret2 = pygame.Rect(random.randint(0, 455), random.randint(0, 355), 45, 45)

        retX = velocidades[random.randint(0, 1)]
        retY = velocidades[random.randint(0, 1)]
        ret2X = velocidades[random.randint(0, 1)]
        ret2Y = velocidades[random.randint(0, 1)]

        bateu = False

    pygame.display.flip()
pygame.quit()
