import time

import pygame
import random
import board as bd
import colors as color
from screen import *
import squads as sq
### INIT

pygame.init()

bd.create_grid()
bd.create_squads()

running = True
while running:
    screen.fill(color.BLACK)  # Fondo suave
      # Dibujar el tablero sin separaciones
    bd.draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bd.Squads["S1"].turn()

        pygame.display.flip()

        for squads in bd.Squads:
            if bd.Squads[squads].ind == 100:
                bd.print_text("Tenemos un ganador!!!!")
                bd.print_subtext("Seguro que son guapisimos...")
                time.sleep(2)
                running = False







pygame.quit()


