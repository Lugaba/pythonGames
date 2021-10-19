# Autor: Felipe Torales Leite e Luca Amelio Hummel
# Tia: 32034539 e 32016816

import random

class Quadrado:
    altura = 0
    largura = 0
    cor = (0,0,0)
    posX = 0
    posY = 0

    def sorteiacor(self):
        self.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def sorteiaX(self):
        self.posX = random.randint(0, 1000)

    def sorteiaY(self):
        self.posY = random.randint(0, 800)