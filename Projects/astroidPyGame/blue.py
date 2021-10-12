import pygame
import random

pygame.init()
pygame.display.set_caption('kinda blue')
screen = pygame.display.set_mode((600, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill((135, 226, 232))
    x = random.randint(10, 580)
    y = random.randint(10, 580)
    r = random.randint(2, 20)

    pygame.draw.circle(screen, (100, 211, 100), (x, y), r)
    pygame.display.flip()
