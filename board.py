import pygame
import random

import squads
from events import *
from init import Squads
from screen import *
from colors import *

### board config
grid_size = 10
square_size = 70
nb_squares = 100
pygame.font.init()

def generate_spiral():
    spiral = [[-1] * grid_size for _ in range(grid_size)]
    x, y = 0, 0
    dx, dy = 0, 1
    for i in range(grid_size * grid_size):
        spiral[x][y] = i
        if (
                0 <= x + dx < grid_size
                and 0 <= y + dy < grid_size
                and spiral[x + dx][y + dy] == -1
        ):
            x += dx
            y += dy
        else:
            dx, dy = dy, -dx
            x += dx
            y += dy
    return spiral

spiral = generate_spiral()
spiral_indices = [spiral[x][y] for x in range(grid_size) for y in range(grid_size) if spiral[x][y] != -1]
def draw_board():
    # squares
    for idx, index in enumerate(spiral_indices):

        square_event = get_event(spiral_indices[index])
        color = event_colors[square_event]
        symbol = event_symbols[square_event]

        x, y = index // grid_size, index % grid_size
        rect_x = x * square_size + 80
        rect_y = y * square_size + 50
        pygame.draw.rect(screen, color=color, rect=(rect_x, rect_y, square_size, square_size))
        pygame.draw.rect(screen, color=BLACK, rect=(rect_x, rect_y, square_size, square_size), width=1)

        font = pygame.font.SysFont(None, 20)
        number_text = font.render(str(spiral_indices[index] + 1), True, BLACK)
        screen.blit(number_text, (rect_x + 5, rect_y + 5))

        symbol_text = font.render(symbol, True, BLACK)
        text_x = rect_x + square_size // 2 - 10
        text_y = rect_y + square_size // 2 - 10
        #screen.blit(symbol_text, (text_x, text_y))

    # lines
    pygame.draw.line(screen, SOFT_BLUE, (320-170, 50), (320-170, 680), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (320-170, 680), (880-170, 680), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (880-170, 680), (880-170, 120), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (880-170, 120), (390-170, 120), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (390-170, 120), (390-170, 610), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (390-170, 610), (810-170, 610), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (810-170, 610), (810-170, 190), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (810-170, 190), (460-170, 190), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (460-170, 190), (460-170, 540), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (460-170, 540), (740-170, 540), width=5)

    pygame.draw.line(screen, SOFT_BLUE, (740-170, 540), (740-170, 260), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (740-170, 260), (530-170, 260), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (530-170, 260), (530-170, 470), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (530-170, 470), (670-170, 470), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (670-170, 470), (670-170, 330), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (670-170, 330), (600-170, 330), width=5)
    pygame.draw.line(screen, SOFT_BLUE, (600-170, 330), (600-170, 400), width=5)


def draw_squads():
    for s in Squads:
        squad = Squads[s]
        x, y = spiral_indices[squad.square - 1] // 10, spiral_indices[squad.square - 1] % 10
        c_x = x * square_size + squad.x
        c_y = y * square_size + squad.y
        pygame.draw.circle(screen, BLACK, center=(c_x, c_y), radius=10)
        pygame.draw.circle(screen, squad.color, center = (c_x, c_y), radius= 8)




