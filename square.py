import pygame

from colors import PASTEL_YELLOW, BLACK
from screen import screen
from events import *

class Square:
    def __init__(self, x, y, ind):
        self.x = x
        self.y = y
        self.size = 70
        self.ind = ind
        self.event = get_event(ind-1)


    def draw(self):
        pygame.draw.rect(screen, color=event_colors[self.event], rect=(self.x, self.y, self.size, self.size))
        pygame.draw.rect(screen, color=BLACK, rect=(self.x, self.y, self.size, self.size), width=1)
        font = pygame.font.SysFont(None, 20)
        number_text = font.render(str(self.ind), True, BLACK)
        screen.blit(number_text, (self.x + 5, self.y + 5))




