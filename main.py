import time

import pygame
import random
import board as bd
import colors as color
import events
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

def checks(squad, id_squad):
    if squad.ind-1 in events.ind_recompensa:
        squad.check_nano()
        squad.check_swap()
        if squad.check_oca():
            bd.draw_board()
            bd.draw_squads()
            squad.card()
            return squad.nb+1
        if squad.check_stones():
            return squad.nb+1

    elif squad.ind-1 in events.ind_castigo:
        squad.check_red()

    return id_squad

def to_color(squad_turn):
    if squad_turn == 1:
        return "rojo"
    if squad_turn == 2:
        return "azul"
    if squad_turn == 3:
        return "amarillo"
    if squad_turn == 4:
        return "verde"

def do_turn_1():
    squad = bd.Squads["S1"]
    bd.print_text("Es el turno del equipo rojo")
    squad.turn()
    bd.draw_board()
    bd.draw_squads()
    squad.card()


def do_turn(id_squad):
    squad = bd.Squads["S"+str(id_squad)]
    bd.print_text("Es el turno del equipo " + to_color(squad_turn))

    if squad.check_block():
        bd.print_text("Adonde vais, traviesos???")
        bd.print_text("Un traguito os hará esto más ameno jeje")
        time.sleep(2)
        if id_squad != bd.nb_squads:
            id_squad += 1
        else:
            id_squad = 1
    else:
        squad.turn()
        bd.draw_board()
        bd.draw_squads()
        squad.card()
        if squad.check_oca():
            bd.draw_board()
            bd.draw_squads()
            squad.card()
            return id_squad
        if squad.check_ladder():
            bd.draw_board()
            bd.draw_squads()

        if id_squad != bd.nb_squads:
            id_squad += 1
        else:
            id_squad = 1
        id_squad = checks(squad, id_squad)

    return id_squad


##### RUN GAME #######
game=True
while running:


    while game:
        bd.draw_board()
        bd.draw_squads()
        bd.print_text("Es el turno del equipo " + to_color(squad_turn))
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                if bd.nb_squads == 1:
                    do_turn_1()
                else:
                    squad_turn = do_turn(squad_turn)

        pygame.display.flip()

        for squads in bd.Squads:
            if bd.Squads[squads].ind == 100:
                pygame.draw.rect(screen, color=color.BLACK, rect=(800, 50, 500, 100))
                pygame.display.flip()
                bd.print_text("Tenemos un ganador!!!!")
                bd.print_subtext("Seguro que son guapisimos...")
                game = False


        clock.tick(60)

    bd.print_text("Gracias por jugar os quieroooo")
    clock.tick(60)





pygame.quit()


