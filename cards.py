import time

import pygame
import random
import events as events
import screen as scr
import colors as color
import board as bd

class Card:
    def __init__(self, text):
        self.text = text

    def draw(self):
        pygame.draw.rect(scr.screen, color.BLACK, rect=(800, 400, 250, 300))
        pygame.draw.rect(scr.screen, color.WHITE, rect=(800, 400, 250, 300), width=2)
        bd.print_cardtext([self.text])



def card_reto():
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.draw.rect(scr.screen, color.WHITE, rect=(800, 400, 250, 300), width=2)
    bd.print_cardtext(['Cartas :D'])




