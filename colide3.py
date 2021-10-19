import pygame, time, math
from random import randint

# inicializando módulos de pygame
pygame.init()
pygame.font.init()
relogio = pygame.time.Clock()

# definindo outras constantes do jogo
LARGURAJANELA = 800
ALTURAJANELA = 450

# criando a janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('Corrida')
x = 350 # coord x do carro do jogador
y = 100 # coord y do carro do jogador
pos_x = 500 # referência inicial X para posicionar os outros carros
pos_y = 1200 # coord inicial y do carro policia
pos_y_a = 800 # coord inicial y do carro preto
pos_y_c = 2000 # coord inicial y carro vermelho

# registros do tempo decorrido
timer = 0
tempo_segundo = 0
velocidade = 10 # velocidade do carro do jogador
velocidade_outros = 12 # velocidade dos outros carros
fundo = pygame.image.load('images/PistaCorrida.jpg')
carro1 = pygame.image.load('images/carro1.png')
carro2 = pygame.image.load('images/carro2.png')
carro3 = pygame.image.load('images/carro3.png')
carro4 = pygame.image.load('images/carro4.png')

# configuração das fontes
fonte = pygame.font.SysFont('Arial Black', 20)
texto = fonte.render("Tempo: ", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)
fonte_perdeu = pygame.font.SysFont('Arial Black', 40)
texto_perdeu = fonte_perdeu.render("GAME OVER", True, (247, 97, 6), (0, 0,
                                                                     0))

# loop do jogo
jogoAtivo = True
bateu = 0
while jogoAtivo:
    pygame.time.delay(50)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogoAtivo = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and x <= 520:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 175:
        x -= velocidade

    # calcula a distância entre dois pontos em relação aos carros
    # distância entre o carro do jogador e o carro da polícia
    dist1 = math.sqrt(math.pow(pos_x - x, 2) + (math.pow(pos_y - y, 2)))

    # distância entre o carro do jogador e o carro preto
    dist2 = math.sqrt(math.pow(x - (pos_x - 300), 2) + (math.pow(y -
                                                                 pos_y_a, 2)))
    # distância entre o carro do jogador e o carro da vermelho
    dist3a = math.sqrt(math.pow((pos_x - 150) - x, 2) + (math.pow(pos_y_c -
                                                                  y, 2)))
    dist3b = math.sqrt(math.pow(x - (pos_x - 150), 2) + (math.pow(y -
                                                                  pos_y_c, 2)))
    #verifica se houve colisão em algum caso
    if dist1 < 100:
        janela.blit(texto_perdeu, (300, 200))
        pygame.display.update()
        bateu = 1
    if dist2 < 100:
        janela.blit(texto_perdeu, (300, 200))
        pygame.display.update()
        bateu = 1
    if dist3a < 100 or dist3b < 100:
        janela.blit(texto_perdeu, (300, 200))
        pygame.display.update()
        bateu = 1

    # se não houve colisão...
    if bateu != 1:
        # quando os carros desaparecem... são programados para reaparecer
        if pos_y <= -170:
            pos_y = randint(800, 1000)
        if pos_y_a <= -170:
            pos_y_a = randint(1300, 2000)
        if pos_y_c <= -170:
            pos_y_c = randint(2300, 3000)
        # aumenta a velocidade
        pos_y -= velocidade_outros
        pos_y_a -= velocidade_outros + 2
        pos_y_c -= velocidade_outros + 10 # carro vermelho
        # atualiza o tempo - a cada 20 ciclos, é passado um minuto
        if timer <= 20:
            timer += 1
        else:
            tempo_segundo += 1
            texto = fonte.render("Tempo: " + str(tempo_segundo), True,
                             (255, 255, 255), (0, 0, 0))
            timer = 0

        # exibe as imagens na tela
        janela.blit(fundo, (0, 0))
        janela.blit(carro1, (x, y))
        janela.blit(carro2, (pos_x, pos_y))
        janela.blit(carro3, (pos_x - 300, pos_y_a))
        janela.blit(carro4, (pos_x - 150, pos_y_c))
        janela.blit(texto, pos_texto)

        # atualizando na tela tudo o que foi desenhado
        pygame.display.update()
    else:
        jogoAtivo = False

pygame.time.delay(2000)
pygame.quit()