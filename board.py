import pygame
import random

import colors
import squads
from events import *
import squads as sq
from screen import *
from colors import *
from square import Square
import cards as crd

### board config
grid_size = 10
square_size = 70
nb_squares = 100
pygame.font.init()

########### CREATION #########



grid = []
ind_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            36, 37, 38, 39, 40, 41, 42, 43, 44, 11,
            35, 64, 65, 66, 67, 68, 69, 70, 45, 12,
            34, 63, 84, 85, 86, 87, 88, 71, 46, 13,
            33, 62, 83, 96, 97, 98, 89, 72, 47, 14,
            32, 61, 82, 95, 100, 99, 90, 73, 48, 15,
            31, 60, 81, 94, 93, 92, 91, 74, 49, 16,
            30, 59, 80, 79, 78, 77, 76, 75, 50, 17,
            29, 58, 57, 56, 55, 54, 53, 52, 51, 18,
            28, 27, 26, 25, 24, 23, 22, 21, 20, 19]

def create_grid():
    rect_x = 80
    k = 0
    for i in range(10):

        rect_y = 50
        for j in range(10):
            grid.append(Square(rect_x, rect_y, ind_list[k]))
            k += 1
            rect_y += 70
        rect_x += 70


def find_square(ind):
    for square in grid:
        if square.ind == ind:
            return square
    return None

Squads = {}
nb_squads = 4
def create_squads():
    for i in range(nb_squads):
        Squads["S" + str(i + 1)] = sq.Squad("Equipo " + str(i + 1), i)


############### DRAWING ######################

def draw_board():
    # squares
    for square in grid:
        square.draw()
    # lines
    pygame.draw.line(screen, BLACK, (320-170, 50), (320-170, 680), width=5)
    pygame.draw.line(screen, BLACK, (320-170, 680), (880-170, 680), width=5)
    pygame.draw.line(screen, BLACK, (880-170, 680), (880-170, 120), width=5)
    pygame.draw.line(screen, BLACK, (880-170, 120), (390-170, 120), width=5)
    pygame.draw.line(screen, BLACK, (390-170, 120), (390-170, 610), width=5)
    pygame.draw.line(screen, BLACK, (390-170, 610), (810-170, 610), width=5)
    pygame.draw.line(screen, BLACK, (810-170, 610), (810-170, 190), width=5)
    pygame.draw.line(screen, BLACK, (810-170, 190), (460-170, 190), width=5)
    pygame.draw.line(screen, BLACK, (460-170, 190), (460-170, 540), width=5)
    pygame.draw.line(screen, BLACK, (460-170, 540), (740-170, 540), width=5)

    pygame.draw.line(screen, BLACK, (740-170, 540), (740-170, 260), width=5)
    pygame.draw.line(screen, BLACK, (740-170, 260), (530-170, 260), width=5)
    pygame.draw.line(screen, BLACK, (530-170, 260), (530-170, 470), width=5)
    pygame.draw.line(screen, BLACK, (530-170, 470), (670-170, 470), width=5)
    pygame.draw.line(screen, BLACK, (670-170, 470), (670-170, 330), width=5)
    pygame.draw.line(screen, BLACK, (670-170, 330), (600-170, 330), width=5)
    pygame.draw.line(screen, BLACK, (600-170, 330), (600-170, 400), width=5)


def draw_squads():
    for s in Squads:
        squad = Squads[s]
        squad.draw()


################# PRINTING ###############

def print_text(str):
    pygame.draw.rect(screen, color=colors.BLACK, rect=(800, 50, 500, 100))
    font = pygame.font.SysFont(None, 25)
    text = font.render(str, True, colors.WHITE)
    screen.blit(text, (800, 50))
    pygame.display.flip()

def print_subtext(str):
    font = pygame.font.SysFont(None, 20)
    text = font.render(str, True, colors.WHITE)
    screen.blit(text, (800, 70))
    pygame.display.flip()

def print_speccardtext(list):
    y = 20
    for str in list:
        if y == 20:
            font = pygame.font.SysFont(None, 40)
            text = font.render(str, True, colors.WHITE)
            screen.blit(text, (810, 300 + y))
            y+=40
        else:
            font = pygame.font.SysFont(None, 25)
            text = font.render(str, True, colors.WHITE)
            screen.blit(text, (810, 300+y))
            y+=20
        #pygame.display.flip()

def print_cardtext(list):
    y = 20
    for str in list:
        font = pygame.font.SysFont(None, 25)
        text = font.render(str, True, colors.WHITE)
        screen.blit(text, (810, 410 + y))
        y += 20