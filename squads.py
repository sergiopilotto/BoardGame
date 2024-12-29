from tkinter.font import names
import random
import pygame
import time
import colors as color
import events as events
import cards as crd
import board as bd
from screen import screen


class Squad:
    def __init__(self, name, nb):
        self.name = name
        self.nb = nb
        self.ind = 0
        self.square = bd.grid[self.ind]
        self.color = color.squad_colors[nb]
        self.x = self.square.x + self.get_x()
        self.y =  self.square.y + self.get_y()
        self.six = []

    def get_x(self):
        if self.nb == 0 or self.nb == 1:
            return 20
        return 50

    def get_y(self):
        if self.nb == 0 or self.nb == 2:
            return 30
        return 55

    def throw_dice(self):
        dice = random.randint(1, 6)
        if dice == 6:
            self.six.append(dice)
        else:
            self.six = []
        return dice

    def card(self):
        self.square.card.draw()

    def move(self, ind):
        if self.check_throws():
            self.square = bd.grid[0]

        elif self.ind + ind > 100:
            self.ind = 100 - (self.ind + ind - 100)
            self.square = bd.find_square(self.ind)
        else:
            self.ind += ind
            self.square = bd.find_square(self.ind)
        self.x = self.square.x + self.get_x()
        self.y = self.square.y + self.get_y()


    def draw(self):
        pygame.draw.circle(screen, color=color.BLACK, center=(self.x, self.y), radius=10)
        pygame.draw.circle(screen, color=self.color, center=(self.x, self.y), radius=8)

    def turn(self):
        dice = self.throw_dice()
        pygame.draw.circle(screen, color.WHITE, (1000, 200), 50)
        font = pygame.font.SysFont(None, 50)
        number_text = font.render(str(dice), True, color.BLACK)
        screen.blit(number_text, (990, 180))
        pygame.display.update()
        self.move(dice)

    def check_throws(self):
        if len(self.six) == 3:
            bd.print_text("Has tirado tres 6 seguidos!!!")
            bd.print_subtext("Espabila anda...")
            time.sleep(2)
            return True
        return False








