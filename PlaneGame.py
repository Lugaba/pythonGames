import pygame
import random
# Controle mais fácil das teclas pressionadas
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define objeto Player estendendo a classe pygame.sprite.Sprite
# A superfície desenhada na tela é um atributo de ‘player’
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Movimenta o Player em função das teclas pressionadas
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Mantém o jogador no limite da tela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define objeto Enemy estendendo a classe pygame.sprite.Sprite
# A superfície desenhada na tela é um atributo de ‘Enemy’
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
        center=(
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
            random.randint(0, SCREEN_HEIGHT),
        )
    )
        self.speed = random.randint(5, 20)

    # Movimenta o sprite baseando-se na velocidade
    # Remove o sprite quando atinge o limite esquerdo da tela
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Cria um evento próprio
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instancia um jogador (agora é um retângulo)
player = Player()

# Cria grupo para armazenar os sprites dos inimigos e todos os sprites
# inimigos são usados para detectar colisão e atualizar as posições
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

jogoAtivo = True
clock = pygame.time.Clock()
while jogoAtivo:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                jogoAtivo = False
        elif event.type == QUIT:
            jogoAtivo = False

        # Adiciona novos inimigos
        elif event.type == ADDENEMY:
            # Cria novo inimigo e adiciona no grupo de sprites
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()

    # atualiza posição do player
    player.update(pressed_keys)

    # atualiza posição dos inimigos
    enemies.update()

    screen.fill((135, 206, 250))

    # Desenha todos os sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Verifica se algum inimigo colidiu com algum inimigo
    if pygame.sprite.spritecollideany(player, enemies):
        # Remove jogador e encerra programa
        player.kill()
        jogoAtivo = False
    # Desenha jogador na tela
    pygame.display.flip()