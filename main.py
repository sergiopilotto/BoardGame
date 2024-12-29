import time

import pygame
import random
import board as bd
import colors as color
from board import nb_squads
from screen import *
import squads as sq
### INIT

pygame.init()

clock = pygame.time.Clock()

bd.create_grid()
bd.create_squads()
squad_turn = 1

running = True
screen.fill(color.BLACK)
while running:



    bd.draw_board()
    bd.draw_squads()
    bd.print_text("Es el turno del equipo " + str(squad_turn))
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        running = False

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:

            if squad_turn == 1:
                bd.print_text("Es el turno del equipo " + str(squad_turn))
                squad = bd.Squads["S1"]
                squad.turn()
                bd.draw_board()
                bd.draw_squads()
                squad.card()
                if squad_turn != bd.nb_squads:
                    squad_turn = 2
                else:
                    squad_turn = 1

            elif squad_turn == 2:
                bd.print_text("Es el turno del equipo " + str(squad_turn))
                squad = bd.Squads["S2"]
                squad.turn()
                bd.draw_board()
                bd.draw_squads()
                squad.card()
                if squad_turn != bd.nb_squads:
                    squad_turn = 3
                else:
                    squad_turn = 1

            elif squad_turn == 3:
                bd.print_text("Es el turno del equipo " + str(squad_turn))
                squad = bd.Squads["S3"]
                squad.turn()
                bd.draw_board()
                bd.draw_squads()
                squad.card()
                if squad_turn != bd.nb_squads:
                    squad_turn = 4
                else:
                    squad_turn = 1

            elif squad_turn == 4:
                bd.print_text("Es el turno del equipo " + str(squad_turn))
                squad = bd.Squads["S4"]
                squad.turn()
                bd.draw_board()
                bd.draw_squads()
                squad.card()
                squad_turn = 1

    pygame.display.flip()

    for squads in bd.Squads:
        if bd.Squads[squads].ind == 100:
            pygame.draw.rect(screen, color=color.BLACK, rect=(800, 50, 500, 100))
            pygame.display.flip()
            bd.print_text("Tenemos un ganador!!!!")
            bd.print_subtext("Seguro que son guapisimos...")


    clock.tick(60)





pygame.quit()


