from tkinter.font import names
import random
import pygame

from colors import squad_colors
from events import *
from cards import *


class Squad:
    def __init__(self, name, nb):
        self.name = name
        self.nb = nb
        self.square = 11
        self.color = squad_colors[nb]
        self.x = self.get_x()
        self.y =  self.get_y()

    def get_x(self):
        if self.nb == 0 or self.nb == 1:
            return 100
        return 130

    def get_y(self):
        if self.nb == 0 or self.nb == 2:
            return 80
        return 105

    def throw_dice(self):
        dice = random.randint(1, 6)
        return dice

    def get_card(self):
        get_event(self.square)
        select_card(self.square)

    def move(self, ind):
        self.square += ind
        self.x = self.square // 10 + self.get_x()
        self.y = self.square % 10 + self.get_y()

    def turn(self):
        dice = self.throw_dice()
        self.move(dice)
        self.get_card()









