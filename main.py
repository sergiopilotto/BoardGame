import pygame
import random
from colors import *
from init import *
from board import *
from screen import *
from squads import *
### INIT

pygame.init()


running = True
while running:
    screen.fill(BLACK)  # Fondo suave
    draw_board()  # Dibujar el tablero sin separaciones
    draw_squads()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Squads["S1"].turn()


    pygame.display.flip()



pygame.quit()


