import pygame

from colors import PASTEL_YELLOW, BLACK
from screen import screen
from events import *
import cards as card

class Square:
    def __init__(self, x, y, ind):
        self.x = x
        self.y = y
        self.size = 70
        self.ind = ind
        self.event = get_event(ind-1)
        #self.card = card.select_card(ind)


    def draw(self):
        pygame.draw.rect(screen, color=event_colors[self.event], rect=(self.x, self.y, self.size, self.size))
        pygame.draw.rect(screen, color=BLACK, rect=(self.x, self.y, self.size, self.size), width=1)
        font = pygame.font.SysFont(None, 20)
        number_text = font.render(str(self.ind), True, BLACK)
        screen.blit(number_text, (self.x + 5, self.y + 5))
        image = select_image(self.ind-1)

        if image is not None:
            screen.blit(image, (self.x + 15, self.y + 20))


def select_image(ind):
    if ind in dict_image.keys():
        image = pygame.image.load(dict_image[ind]).convert_alpha()
        return pygame.transform.scale(image, (40, 40))
    return None


