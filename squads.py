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
        self.ind = 93
        self.square = bd.grid[0]
        self.color = color.squad_colors[nb]
        self.x = self.square.x + self.get_x()
        self.y =  self.square.y + self.get_y()
        self.six = []
        self.last_dice = 0
        self.turns_blocked = 0

    def get_x(self):
        if self.nb == 0 or self.nb == 1:
            return 20
        return 50

    def get_y(self):
        if self.nb == 0 or self.nb == 2:
            return 30
        return 55

    def update_pos(self):
        self.square = bd.find_square(self.ind)
        self.x = self.square.x + self.get_x()
        self.y = self.square.y + self.get_y()

    def throw_dice(self):
        dice = random.randint(1, 1)
        self.last_dice = dice
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
        #time.sleep(1.5)
        self.move(dice)

    def check_block(self):
        if self.turns_blocked != 0:
            self.turns_blocked -= 1
            return True
        return False

    def check_throws(self):
        if len(self.six) == 3:
            bd.print_text("Has tirado tres 6 seguidos!!!")
            bd.print_subtext("Espabila anda...")
            time.sleep(2)
            return True
        return False

    def check_oca(self):
        if self.ind-1 == events.ind_oca[-1]:
            bd.print_text("Oh! Una oca loca!!!!!")
            bd.print_subtext("Pero es la ultima oca...")
            time.sleep(3)
            return False

        for i_oca in range(len(events.ind_oca)):
            if self.ind-1 == events.ind_oca[i_oca]:
                bd.print_text("Oh! Una oca loca!!!!!")
                bd.print_subtext("Curiosete...")
                time.sleep(2)
                self.ind = events.ind_oca[i_oca + 1]+1
                self.update_pos()
                return True

    def check_ladder(self):
        if self.ind == 13:
            bd.print_text("Escalera!!! ARRIBAAAA")
            bd.print_subtext("Qué cabrones...")
            time.sleep(2)
            self.ind = 44
            self.update_pos()
            return True
        if self.ind == 44:
            bd.print_text("Escalera!!! ABAJO >:)")
            bd.print_subtext("Callao...")
            time.sleep(3)
            self.ind = 13
            self.update_pos()
            return True
        return False

    def check_nano(self):
        if self.ind == 14:
            bd.print_text("EL NANO AE, EL NANO AO")
            bd.print_subtext("Ojito con 2026... Shhh!!!!")
            time.sleep(3)
            self.move(self.last_dice)
            bd.draw_board()
            bd.draw_squads()
            self.card()
    def check_swap(self):
        if self.ind == 14:
            bd.print_text("EL NANO AE, EL NANO AO")
            bd.print_subtext("Ojito con 2026... Shhh!!!!")
            time.sleep(3)
            self.move(self.last_dice)
            bd.draw_board()
            bd.draw_squads()
            self.card()
        if self.ind == 40:
            bd.print_text("CAMBIO")
            time.sleep(3)
            ind1 = self.ind
            i = random.randint(1, 4)
            while i == self.nb+1:
                i = random.randint(1, 4)
            ind2 = bd.Squads["S"+str(i)].ind
            self.ind = ind2
            bd.Squads["S"+str(i)].ind = ind1
            self.update_pos()
            bd.Squads["S"+str(i)].update_pos()
            self.check_oca()
            self.check_block()
            self.check_ladder()
            self.check_red()




    def check_stones(self):
        if self.ind == 25 or self.ind == 50:
            bd.print_text("OTRA")
            bd.print_subtext("Qué perros...")
            time.sleep(3)
            return True
        return False


    def check_red(self):
        # blocking turns
        if self.ind == 10:
            bd.print_text("Ayyyyyy, una pena eh")
            bd.print_subtext("Ojala sea Helena...")
            time.sleep(3)
            self.turns_blocked = 1
            return True
        if self.ind == 30:
            bd.print_text("Ayyyyyy, una pena eh")
            bd.print_subtext("Ojala sea Helena...")
            time.sleep(3)
            self.turns_blocked = 2
            return True
        if self.ind == 54:
            bd.print_text("Ayyyyyy, una pena eh")
            bd.print_subtext("Ojala sea Helena...")
            time.sleep(3)
            self.turns_blocked = 3
            return True
        if self.ind == 74:
            bd.print_text("Ayyyyyy, una pena eh")
            bd.print_subtext("Ojala sea Helena...")
            time.sleep(3)
            self.turns_blocked = 4
            return True
        # the rest
        elif self.ind == 62:
            bd.print_text("Nada nada, a pastar")
            bd.print_subtext("Lo que el alcohol te da, el alcohol te lo quita...")
            time.sleep(3)
            self.ind = 29
            self.update_pos()
            return True
        elif self.ind == 96:
            bd.print_text("Sorpresa!!!! Os vais para abajo XD")
            bd.print_subtext("Comemierdas...")
            time.sleep(3)
            self.ind = 69
            self.update_pos()
            return True
        elif self.ind == 89:
            bd.print_text("Hostia estáis bien??? No me lloreis tampoco eh")
            bd.print_subtext("Por dios ojalá sea Helena eh salto de la alegría como sea Helena")
            time.sleep(3)
            self.ind = 1
            self.update_pos()
            return True







