import time

import pygame
import random
import events as events
import screen as scr
import colors as color
import board as bd

class Card:
    def __init__(self, text, image):
        self.text = text
        self.image = image

    def draw(self):
        pygame.draw.rect(scr.screen, color.BLACK, rect=(800, 300, 380, 450))
        pygame.draw.rect(scr.screen, color.WHITE, rect=(800, 300, 380, 450), width=2)
        if self.image is not None:
            image = pygame.image.load(self.image)
            image = pygame.transform.scale(image, (250, 250))
            scr.screen.blit(image, (865, 470))

        bd.print_cardtext(self.text)





dict_cards = {
    4: Card(['Oca', "De oca en oca y tiro porque me toca!", "También mandáis cada uno un trago"],
            "icons/goose.png"),
    7: Card(["Alex", "Alex se ha ganado un chupito!", "Qué envidia..."],
            "icons/alex.jpg"),
    8: Card(["Sophie", "Sophie se ha ganado un chupito!", "Qué envidia..."],
            "icons/sophie.jpg"),
    9: Card(['Oca', "De oca en oca y tiro porque me toca!", "También mandáis cada uno un trago"],
            "icons/duck-face.png"),
    10: Card(['Hoguera', "Os quedáis aquí un turno!", "Y que no se os olvide beber en cada turno..."],
             "icons/bonfire.png"),
    11: Card(['Ana', "Ana se ha ganado un chupito!", "Qué envidia..."],
             "icons/ana.jpg"),
    13: Card(['Escalera', "Ole! Avanzáis hasta la casilla 44"],
             "icons/ladder_inverted.png"),
    14: Card(["Fernando Alonso", "Avanzais otra vez con la misma tirada!", "La putísima cabra dios mío", "Mandáis un trago!"],
             "icons/nano.jpg"),
    16: Card(["Cowboy >:)", "Disparáis 6 tragos a quien queráis"],
             "icons/cowboy.png"),
    19: Card(["Lucía", "Lucía se ha ganado un chupito!", "Qué envidia..."],
             "icons/lucia.jpg"),
    20: Card(["Oca", "De oca en oca y tiro porque me toca!", "También mandáis cada uno un trago eh"],
             "icons/ugly-goose.jpeg"),
    24: Card(["Elsa", "Elsa se ha ganado un chupito!", "Qué envidia..."],
             "icons/elsa.jpg"),
    25: Card(["Pedro Sánchez", "Hacéis la del perro y tiráis otra vez!", "Mandáis un trago!"],
             "icons/perro-sanxe.jpg"),
    29: Card(["Oca (Grey Goose)", "De oca en oca y tiro porque me toca!", "También mandáis cada uno un trago"],
             "icons/grey-goose.jpg"),
    30: Card(["El Pozo", "Os quedáis aquí dos turnos!", "Y que no se os olvide beber en cada turno..."],
             "icons/elpozo.jpg"),
    33: Card(["Paco", "Paco se ha ganado un chupito!", "Qué envidia..."],
             "icons/paco.jpg"),
    36: Card(["Oca", "De oca en oca y tiro porque me toca!", "También mandáis cada uno un trago"],
             "icons/hipster-goose.jpg"),
    40: Card(["Swap", "Cambiais de posición con un equipo", "aleatorio!", "Y también mandáis un trago!"],
             "icons/swap.png"),
    44: Card(["Escalera", "Ayyyy... Retrocedéis hasta la casilla 13!"],
             "icons/ladder_inverted.png"),
    45: Card(["Oca", "De oca en oca y tiro porque me toca!", "También mandais cada uno un trago eh"],
             "icons/crazy-goose.jpg"),
    49: Card(["Elisa", "Elisa se ha ganado un chupito!", "Qué envidia..."],
             "icons/elisa.jpg"),
    50: Card(["Pierre", "En honor a Pierre, volvéis a tirar", "y mandéis un trago!", "A este también le gusta repetir..."],
             "icons/pierre.jpg"),
    54: Card(["Carcél", "Os quedáis aquí tres turnos!", "Y que no se os olvide beber en cada turno..."],
             "icons/prisoner.png"),
    58: Card(["Salomé", "Salomé se ha ganado un chupito!", "Qué envidia..."],
             "icons/salome.jpg"),
    60: Card(["Oca", "De oca en oca y tiro porque me toca!", "También mandais cada uno un trago eh"],
             "icons/cool-goose.jpg"),
    62: Card(["Resaca", "Volvéis a la casilla Grey Goose!!!", "Lo que el alcohol te da, el alcohol te lo ", "quita..."],
             "icons/vomit.png"),
    65: Card(["Última Oca!", "No hay más ocas después de esta, así que ","solo os dejo mandar un trago",],
             "icons/strong-goose.jpg"),
    68: Card(["Helena", "Helena se ha ganado un chupito!", "Que se joda..."],
             "icons/helena.jpg"),
    72: Card(["Espejo", "La próxima vez que os toque beber, le ", "podéis mandar los tragos a otra persona!"],
             "icons/magic-mirror.png"),
    74: Card(["Laberinto", "Os quedáis aquí cuatro turnos!", "Y que no se os olvide beber en cada turno..."],
             "icons/maze_inverted.png"),
    76: Card(["Tiburón", "Repartís 12 tragos!", "El tiburón no tiene nada que ver pero me ", "apetecía poner uno"],
             "icons/shark.png"),
    78: Card(["Combo x2", "A partir de ahora, bebéis el doble de lo que ", "os toque beber!"],
             "icons/bet.png"),
    83: Card(["Diablo", "Todos beben 4 tragos menos vosotros!", "Pero si alguien se atreve a tomarse un ", "chupito, bebéis vosotros..."],
             "icons/devil.png"),
    84: Card(["Blackjack", "Vuestro equipo tiene que beber nada más ", "y nada menos que 21 tragos!", "Os los repartís como queráis..."],
             "icons/game.png"),
    87: Card(["Chupitos", "Cada integrante del equipo se toma un ", "chupito!", "Duro..."],
             "icons/shots.png"),
    88: Card(["Kobe!", "Le lanzáis un chupito a quien queráis"],
             "icons/kobe.jpg"),
    89: Card(["Muerte", "Vaya, la habéis palmao!!!", "Empezáis de nuevo..."],
             "icons/grim-reaper.png"),
    96: Card(["Regalo", "Hala, os vais a la casilla 69!!!"],
             "icons/gift_inverted.png"),
    98: Card(["Sergio", "Sergio se ha ganado un chupito!", "Bien por él!"],
             "icons/yo.jpg"),
    99: Card(["Pedro", "Pedro se ha ganado un chupito!", "Qué envidia..."],
             "icons/pedro.jpg"),
    100: Card(["VICTORIA"],
              "icons/success.png")


}

def select_card(ind):
    if ind in dict_cards.keys():
        return dict_cards[ind]
    else:
        return Card([str(ind)], None)




