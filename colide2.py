import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
VERDE = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Raquetes')

# cria um rect para a bola
square = pygame.Rect(300, 230, 20, 20)

# cria rect para as raquetes
left_pad = pygame.Rect(20, 210, 20, 60)
right_pad = pygame.Rect(600, 210, 20, 60)
pads = [left_pad, right_pad]
velocity_x = 0.5
clock = pygame.time.Clock()

jogoAtivo = True
while jogoAtivo:
    dt = clock.tick(100)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogoAtivo = False

    # movimenta a bola usando o clock como parâmetro para x
    square.move_ip(velocity_x * dt, 0)

    # verifica se houve colisão com as raquetes
    if square.collidelist(pads) >= 0:
        velocity_x = -velocity_x
    screen.fill(BLACK)

    # desenha a bolinha
    pygame.draw.ellipse(screen, VERDE, square, 0)

    # desenha as raquetes
    for pad in pads:
        pygame.draw.rect(screen, WHITE, pad)
    pygame.display.flip()
pygame.quit()