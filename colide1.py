import pygame, time


PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
ROSA = (253, 147, 226)
BRANCO = (255, 255, 255)

LARGURAJANELA = 500
ALTURAJANELA = 400

pygame.init()
pygame.font.init()
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('Movendo com o mouse')

relogio = pygame.time.Clock()
ret = pygame.Rect(10, 10, 45, 45)
ret2 = pygame.Rect(210, 175, 80, 50)
padrao = pygame.font.get_default_font()
fonte = pygame.font.SysFont(padrao, 30)

deve_continuar = True
# loop do jogo
while deve_continuar:
    # checando se ocorreu um evento QUIT
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    relogio.tick(100)
    janela.fill(PRETO)

    # guarda a última posição antes da colisão
    (xant, yant) = (ret.left, ret.top)
    (ret.left, ret.top) = pygame.mouse.get_pos()
    ret.left -= int(ret.width / 2)
    ret.top -= int(ret.height / 2)

    # se houver colisão, exibe mensagem e retorna à posição anterior
    if ret.colliderect(ret2):
        (ret.left, ret.top) = (xant, yant)
        text = fonte.render('COLIDIU!', 1, BRANCO)
        janela.blit(text, (235, 10))
    pygame.draw.rect(janela, VERDE, ret)
    pygame.draw.rect(janela, ROSA, ret2)
    pygame.display.update()
    time.sleep(0.02)

pygame.quit()
