import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Maratonista')
clock = pygame.time.Clock()

while True:
    # Aqui:
    # Desenha todos os nossos elementos
    # Atualiza tudo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    pygame.display.update()
    clock.tick(60)