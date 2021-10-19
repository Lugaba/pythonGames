import pygame
pygame.init()
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("Ola Mundo")
screen.fill((0,255,0))


pygame.draw.rect(screen,(65, 105, 225),(0, 0, 300, 300), 0)

pygame.draw.line(screen,(255, 255, 255),(100, 0),(100,300), 3)
pygame.draw.line(screen,(255, 255, 255),(200, 0),(200,300), 3)
pygame.draw.line(screen,(255, 255, 255),(0, 100),(300,100), 3)
pygame.draw.line(screen,(255, 255, 255),(0, 200),(300,200), 3)

pygame.draw.circle(screen,(255, 255, 0),(150, 150),20, 20)

pygame.display.flip() # atualiza o status da tela
pygame.time.delay(5000)
pygame.quit()