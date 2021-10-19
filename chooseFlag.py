import pygame

print("1- Guiné\n2- Alemanha\n3- Laos")
resposta = input("Qual bandeira deverá ser exibida? ")

pygame.init()
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("Ola Mundo")
screen.fill((0,255,0))

if resposta == "1":
    pygame.draw.rect(screen, (255,0,0), (0,0, 200, 300), 0)
    pygame.draw.rect(screen, (255, 219, 88), (200, 0, 200, 300), 0)
    pygame.draw.rect(screen, (0, 128, 0), (400, 0, 200, 300), 0)
elif resposta == "2":
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, 100), 0)
    pygame.draw.rect(screen, (255, 0, 0), (0, 100, 600, 100), 0)
    pygame.draw.rect(screen, (255, 219, 88), (0, 200, 600, 100), 0)
else:
    pygame.draw.rect(screen, (255, 105, 97), (0, 0, 600, 50), 0)
    pygame.draw.rect(screen, (18, 10, 143), (0, 50, 600, 200), 0)
    pygame.draw.rect(screen, (255, 105, 97), (0, 250, 600, 50), 0)
    pygame.draw.circle(screen, (255, 255, 255), (300, 150), 80, 80)
pygame.display.flip() # atualiza o status da tela
pygame.time.delay(5000)
pygame.quit()