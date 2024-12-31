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
        self.image = "icons/question.png"

    def draw(self):
        pygame.draw.rect(scr.screen, color.BLACK, rect=(800, 300, 380, 450))
        pygame.draw.rect(scr.screen, color.WHITE, rect=(800, 300, 380, 450), width=2)
        if self.image is not None:
            image = pygame.image.load(self.image)
            image = pygame.transform.scale(image, (100, 100))
            scr.screen.blit(image, (940, 310))

        bd.print_cardtext(self.text)

class SpecCard:
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

        bd.print_speccardtext(self.text)





dict_spec_cards = {
    4: SpecCard(['Oca', "De oca en oca y tiro porque me toca!", "También mandáis cada uno un trago"],
            "icons/goose.png"),
    7: SpecCard(["Alex", "Alex se ha ganado un chupito!", "Qué envidia..."],
            "icons/alex.jpg"),
    8: SpecCard(["Sophie", "Sophie se ha ganado un chupito!", "Qué envidia..."],
            "icons/sophie.jpg"),
    9: SpecCard(['Oca', "De oca en oca y tiro porque me toca!", "También mandáis cada uno un trago"],
            "icons/duck-face.png"),
    10: SpecCard(['Hoguera', "Os quedáis aquí un turno!", "Y que no se os olvide beber en cada turno..."],
             "icons/bonfire.png"),
    11: SpecCard(['Ana', "Ana se ha ganado un chupito!", "Qué envidia..."],
             "icons/ana.jpg"),
    13: SpecCard(['Escalera', "Ole! Avanzáis hasta la casilla 44"],
             "icons/ladder_inverted.png"),
    14: SpecCard(["Fernando Alonso", "Avanzais otra vez con la misma tirada!", "La putísima cabra dios mío", "Mandáis un trago!"],
             "icons/nano.jpg"),
    16: SpecCard(["Cowboy >:)", "Disparáis 6 tragos a quien queráis"],
             "icons/cowboy.png"),
    19: SpecCard(["Lucía", "Lucía se ha ganado un chupito!", "Qué envidia..."],
             "icons/lucia.jpg"),
    20: SpecCard(["Oca", "De oca en oca y tiro porque me toca!", "También mandáis cada uno un trago eh"],
             "icons/ugly-goose.jpeg"),
    24: SpecCard(["Elsa", "Elsa se ha ganado un chupito!", "Qué envidia..."],
             "icons/elsa.jpg"),
    25: SpecCard(["Pedro Sánchez", "Hacéis la del perro y tiráis otra vez!", "Mandáis un trago!"],
             "icons/perro-sanxe.jpg"),
    29: SpecCard(["Oca (Grey Goose)", "De oca en oca y tiro porque me toca!", "También mandáis cada uno un trago"],
             "icons/grey-goose.jpg"),
    30: SpecCard(["El Pozo", "Os quedáis aquí dos turnos!", "Y que no se os olvide beber en cada turno..."],
             "icons/elpozo.jpg"),
    33: SpecCard(["Paco", "Paco se ha ganado un chupito!", "Qué envidia..."],
             "icons/paco.jpg"),
    36: SpecCard(["Oca", "De oca en oca y tiro porque me toca!", "También mandáis cada uno un trago"],
             "icons/hipster-goose.jpg"),
    40: SpecCard(["Swap", "Cambiais de posición con un equipo", "aleatorio!", "Y también mandáis un trago!"],
             "icons/swap.png"),
    44: SpecCard(["Escalera", "Ayyyy... Retrocedéis hasta la casilla 13!"],
             "icons/ladder_inverted.png"),
    45: SpecCard(["Oca", "De oca en oca y tiro porque me toca!", "También mandais cada uno un trago eh"],
             "icons/crazy-goose.jpg"),
    49: SpecCard(["Elisa", "Elisa se ha ganado un chupito!", "Qué envidia..."],
             "icons/elisa.jpg"),
    50: SpecCard(["Pierre", "En honor a Pierre, volvéis a tirar", "y mandéis un trago!", "A este también le gusta repetir..."],
             "icons/pierre.jpg"),
    54: SpecCard(["Carcél", "Os quedáis aquí tres turnos!", "Y que no se os olvide beber en cada turno..."],
             "icons/prisoner.png"),
    58: SpecCard(["Salomé", "Salomé se ha ganado un chupito!", "Qué envidia..."],
             "icons/salome.jpg"),
    60: SpecCard(["Oca", "De oca en oca y tiro porque me toca!", "También mandais cada uno un trago eh"],
             "icons/cool-goose.jpg"),
    62: SpecCard(["Resaca", "Volvéis a la casilla Grey Goose!!!", "Lo que el alcohol te da, el alcohol te lo ", "quita..."],
             "icons/vomit.png"),
    65: SpecCard(["Última Oca!", "No hay más ocas después de esta, así que ","solo os dejo mandar un trago",],
             "icons/strong-goose.jpg"),
    68: SpecCard(["Helena", "Helena se ha ganado un chupito!", "Que se joda..."],
             "icons/helena.jpg"),
    72: SpecCard(["Espejo", "La próxima vez que os toque beber, le ", "podéis mandar los tragos a otra persona!"],
             "icons/magic-mirror.png"),
    74: SpecCard(["Laberinto", "Os quedáis aquí cuatro turnos!", "Y que no se os olvide beber en cada turno..."],
             "icons/maze_inverted.png"),
    76: SpecCard(["Tiburón", "Repartís 12 tragos!", "El tiburón no tiene nada que ver pero me ", "apetecía poner uno"],
             "icons/shark.png"),
    78: SpecCard(["Combo x2", "A partir de ahora, bebéis el doble de lo que ", "os toque beber!"],
             "icons/bet.png"),
    83: SpecCard(["Diablo", "Todos beben 4 tragos menos vosotros!", "Pero si alguien se atreve a tomarse un ", "chupito, bebéis vosotros..."],
             "icons/devil.png"),
    84: SpecCard(["Blackjack", "Vuestro equipo tiene que beber nada más ", "y nada menos que 21 tragos!", "Os los repartís como queráis..."],
             "icons/game.png"),
    87: SpecCard(["Chupitos", "Cada integrante del equipo se toma un ", "chupito!", "Duro..."],
             "icons/shots.png"),
    88: SpecCard(["Kobe!", "Le lanzáis un chupito a quien queráis"],
             "icons/kobe.jpg"),
    89: SpecCard(["Muerte", "Vaya, la habéis palmao!!!", "Empezáis de nuevo..."],
             "icons/grim-reaper.png"),
    96: SpecCard(["Regalo", "Hala, os vais a la casilla 69!!!"],
             "icons/gift_inverted.png"),
    98: SpecCard(["Sergio", "Sergio se ha ganado un chupito!", "Bien por él!"],
             "icons/yo.jpg"),
    99: SpecCard(["Pedro", "Pedro se ha ganado un chupito!", "Qué envidia..."],
             "icons/pedro.jpg"),
    100: SpecCard(["VICTORIA"],
              "icons/success.png")


}

deck_cards= [
    Card(['Cuando es el cumple de Sergio?', 'Sergio elige quién del equipo responde!']),
    Card(['Cuando es el cumple de Alex?', 'Alex elige quién del equipo responde!']),
    Card(['Cuando es el cumple de Salomé?', 'Salomé elige quién del equipo responde!']),
    Card(['Cuando es el cumple de Sophie?', 'Sophie elige quién del equipo responde!']),
    Card(['Cuando es el cumple de Elsa?', 'Elsa elige quién del equipo responde!']),
    Card(['Cuando es el cumple de Ana?', 'Ana elige quién del equipo responde!']),
    Card(['Cuando es el cumple de Lucía?', 'Lucía elige quién del equipo responde!']),
    Card(['Cuando es el cumple de Pedro?', 'Pedro elige quién del equipo responde!']),
    Card(['Cuando es el cumple de Paco?', 'Paco elige quién del equipo responde!']),
    Card(['Cuando es el cumple de Elisa?', 'Elisa elige quién del equipo responde!']),
    Card(['Cuando es el cumple de Helena?', 'Helena elige quién del equipo responde!']),
    Card(['Uno de vosotros tiene que haceros adivinar', 'una peli... haciendo mimos!!!',
          'Alguien ajeno al equipo le dice una peli ','al oído al mimo.', 'Tenéis 30 segundos!']),
    Card(['No podéis decir el nombre de nadie en 3 ', 'rondas. Cada vez que lo hagáis, bebéis!!!']),
    Card(['Contad un chiste. Quien se ría, bebe,', 'pero si nadie se ríe vosotros bebéis.']),
    Card(['Decid algo que os cuesta admitir sobre', 'vosotros mismos.']),
    Card(['Dadle un consejo a... Alex!']),
    Card(['Dadle un consejo a... Sergio!']),
    Card(['Dadle un consejo a... Salomé!']),
    Card(['Dadle un consejo a... Sophie!']),
    Card(['Dadle un consejo a... Lucía!']),
    Card(['Dadle un consejo a... Ana!']),
    Card(['Dadle un consejo a... Pedro!']),
    Card(['Dadle un consejo a... Paco!']),
    Card(['Dadle un consejo a... Elsa!']),
    Card(['Dadle un consejo a... Helena!']),
    Card(['Dadle un consejo a... Elisa!']),
    Card(['Decid algo que os guste de... Alex!']),
    Card(['Decid algo que os guste de... Sergio!']),
    Card(['Decid algo que os guste de... Salomé!']),
    Card(['Decid algo que os guste de... Sophie!']),
    Card(['Decid algo que os guste de... Paco!']),
    Card(['Decid algo que os guste de... Pedro!']),
    Card(['Decid algo que os guste de... Lucía!']),
    Card(['Decid algo que os guste de... Elisa!']),
    Card(['Decid algo que os guste de... Elsa!']),
    Card(['Decid algo que os guste de... Helena!']),
    Card(['Decid algo que os guste de... Ana!']),
    Card(['Ronda de Yo Nunca!']),
    Card(['La persona más cabezota bebe!']),
    Card(['La persona más gamer bebe!']),
    Card(['La persona más cinéfila bebe!']),
    Card(['La persona más lectora bebe!']),
    Card(['La persona más culta bebe!']),
    Card(['La persona más sinvergüenza bebe!']),
    Card(['La persona más hipocondríaca bebe!']),
    Card(["La persona más 'overthinker' bebe!"]),
    Card(["Quien se ría en los próximos 3 turnos bebe!"]),
    Card(["Si casualmente hoy es Noche Vieja ", "(o Año Nuevo, aquí nadie se salva), todos", "beben!"]),
    Card(["Ni sí ni no durante los próximos 3 turnos! ", "Si no, bebes ;)"]),
    Card(["Cada persona del equipo elige otra persona.", "Bebéis juntos."]),
    Card(["Contad la vez en la que más os habéis reído!"]),
    Card(["Venga, contad algo que os guste de ","vosotros mismos :)"]),
    Card(["Quién es la persona que más os inspira?"]),
    Card(["Qué es algo que os suele enfadar pero que", "en el fondo sabéis que no es para tanto?"]),
    Card(["Decid una red flag y una green flag."]),
    Card(["Decid algo que hayáis aprendido este año!"]),
    Card(["El que tenga el tiempo de pantalla más alto bebe!"]),
    Card(["Imitad a la persona de vuestra derecha ", "durante 3 rondas.", "Os tendréis que hacer pasar por ella!"]),
    Card(["Cada persona del equipo le tiene que hacer ", "un baile sexy a una persona de su elección."]),
    Card(["Me estoy quedando sin ideas, así que ", "los del equipo hacen un hidalgo."]),
    Card(["Jugad al pistolero, beben todos menos el", "último que quede!"]),
    Card(["La última persona en haber bebido vuelve", "a beber!"]),
    Card(["La persona con la risa más graciosa bebe."]),
    Card(["Las personas que hayan corrido más de 5km", "beben!"]),
    Card(["Empezad a decir marcas de coches, si te", "quedas sin, bebes!", "Continuad hasta que solo quede uno."]),
    Card(["Los que tengan el carné de conducir beben!"]),
    Card(["Los que tengan un doble grado beben", "(vacilando)."]),



]

deck = deck_cards


def select_card(ind):
    global deck
    if ind in dict_spec_cards.keys():
        return dict_spec_cards[ind]
    else:
        #return deck[-1]
        if len(deck) == 0:
            deck = deck_cards.copy()
        card = random.choice(deck)
        deck.remove(card)
        return card




