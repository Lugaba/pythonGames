import pygame
from pygame.locals import *
from random import randint

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Pandemia")
JogoAtivo = True

# TELAS/var
telaAtual = 0
mutado = False
pontos = 0

# IMAGENS
mutadoImg = "Images/mutado.png"
volumeImg = "Images/volume.png"
questionImg = "Images/question 1.png"
botaoImg = "Images/botaoJogar.png"
voltarImg = "Images/voltarBotao.png"

handwashIcon = "Images/handwashIcon.png"
maosIcon = "Images/maosIcon.png"
maskIcon = "Images/maskIcon.png"
vaccineIcon = "Images/vaccineIcon.png"
virusIcon = "Images/virusIcon.png"

mutadoCarregado = pygame.image.load(mutadoImg)
volumeCarregado = pygame.image.load(volumeImg)
questionCarregado = pygame.image.load(questionImg)
botaoCarregado = pygame.image.load(botaoImg)
voltarCarregado = pygame.image.load(voltarImg)


imagensQueda = [[pygame.image.load(handwashIcon), randint(64, 1016), randint(-1000, -100)], [pygame.image.load(maosIcon), randint(64, 1016),
                randint(-1000, -100)], [pygame.image.load(maskIcon), randint(64, 1016), randint(-1000, -100)], [pygame.image.load(vaccineIcon), randint(64, 1016), randint(-1000, -100)],
                [pygame.image.load(virusIcon), randint(64, 1016), randint(-1000, -100)]]

# CORES
azul = (100, 181, 246)
white = (255, 255, 255)

# TEXTOS
my_font = pygame.font.Font("Fonts/SeymourOne-Regular.ttf", 100)
my_font80 = pygame.font.Font("Fonts/SeymourOne-Regular.ttf", 80)
my_font40 = pygame.font.Font("Fonts/SeymourOne-Regular.ttf", 40)
titulo = my_font.render("PANDEMIA", True, white)
tituloManual = my_font80.render("Como jogar?", True, white)


def carregarMenu():
    global JogoAtivo
    global telaAtual
    global mutado

    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if (128 < mouseX < 192) and (636 < mouseY < 700):
                telaAtual = 1
            if (34 < mouseX < 98) and (636 < mouseY < 700):
                mutado = not mutado
            if (415 < mouseX < 664) and (360 < mouseY < 458):
                telaAtual = 2

    screen.fill(azul)

    for i in imagensQueda:
        screen.blit(i[0], (i[1], i[2]))
        i[2] += 0.4
        if i[2] > 780:
            i[1] = randint(64, 1016)
            i[2] = randint(-1000, -100)

    screen.blit(titulo, (540 - titulo.get_width() / 2, 78))
    if not mutado:
        screen.blit(volumeCarregado, (34, 636))
    else:
        screen.blit(mutadoCarregado, (34, 636))
    screen.blit(questionCarregado, (128, 636))
    screen.blit(botaoCarregado, (415, 360))

    pygame.display.update()

def carregarManual():
    global JogoAtivo
    global telaAtual
    global mutado

    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if (34 < mouseX < 98) and (20 < mouseY < 84):
                telaAtual = 0
            if (34 < mouseX < 98) and (636 < mouseY < 700):
                mutado = not mutado

    screen.fill(azul)
    screen.blit(tituloManual, (540 - tituloManual.get_width() / 2, 8))
    screen.blit(voltarCarregado, (34, 20))
    if not mutado:
        screen.blit(volumeCarregado, (34, 636))
    else:
        screen.blit(mutadoCarregado, (34, 636))

    pygame.display.update()

def carregarJogo():
    global JogoAtivo
    global telaAtual
    global mutado
    global pontos
    pontosText = my_font40.render(f"Pontos: {pontos}", True, white)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pontos += 1
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if (34 < mouseX < 98) and (20 < mouseY < 84):
                telaAtual = 0
            if (34 < mouseX < 98) and (636 < mouseY < 700):
                mutado = not mutado

    screen.fill(azul)
    screen.blit(voltarCarregado, (34, 20))
    screen.blit(pontosText, (540 - pontosText.get_width() / 2, 16))
    if not mutado:
        screen.blit(volumeCarregado, (34, 636))
    else:
        screen.blit(mutadoCarregado, (34, 636))

    pygame.display.update()

while JogoAtivo:
    if telaAtual == 0:
        carregarMenu()
    elif telaAtual == 1:
        carregarManual()
    else:
        carregarJogo()


pygame.time.delay(1000)
pygame.quit()

