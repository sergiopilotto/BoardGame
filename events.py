import random

PASTEL_YELLOW = (255, 239, 186)
PASTEL_RED = (255, 200, 200)
PASTEL_GREEN = (200, 255, 200)
GOLD = (255, 215, 0)
SOFT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)

EVENT_TYPES = ["Reto", "Castigo", "Recompensa", "Premio"]
event_colors = {"Reto": PASTEL_YELLOW, "Castigo": PASTEL_RED, "Recompensa": PASTEL_GREEN, "Premio": GOLD}
event_symbols = {"Reto": "?", "Castigo": "X", "Recompensa": "$", "Premio": "W"}


ind_recompensa = [3, 8, 13, 15, 19, 24, 28, 35, 39, 44, 49, 59, 64, 71, 75, 82, 87]
image_recompensa = [3, 8, 13, 15, 19, 24, 28, 35, 39, 44, 49, 59, 64, 71, 75, 82, 87]



ind_castigo = [9, 29, 39, 53, 61, 73, 77, 83, 86, 88, 95]
dict_image = {3:"icons/goose.png",
              6:"icons/alex.jpg",
              7:"icons/sophie.jpg",
              8:"icons/duck-face.png",
              9:"icons/bonfire.png",
              10:"icons/ana.jpg",
              12:"icons/ladder.png",
              13:"icons/nano.jpg",
              15:"icons/cowboy.png",
              18:"icons/lucia.jpg",
              19:"icons/ugly-goose.jpeg",
              23:"icons/elsa.jpg",
              24:"icons/perro-sanxe.jpg",
              28:"icons/grey-goose.jpg",
              29:"icons/elpozo.jpg",
              32:"icons/paco.jpg",
              35:"icons/hipster-goose.jpg",
              39:"icons/swap.png",
              43:"icons/ladder.png",
              44:"icons/crazy-goose.jpg",
              48:"icons/elisa.jpg",
              49:"icons/pierre.jpg",
              53:"icons/prisoner.png",
              57: "icons/salome.jpg",
              59:"icons/cool-goose.jpg",
              61:"icons/vomit.png",
              64:"icons/strong-goose.jpg",
              67:"icons/helena.jpg",
              71:"icons/magic-mirror.png",
              73:"icons/maze.png",
              75:"icons/shark.png",
              77:"icons/bet.png",
              82:"icons/devil.png",
              83:"icons/game.png",
              86:"icons/shots.png",
              87:"icons/kobe.jpg",
              88:"icons/grim-reaper.png",
              95:"icons/gift.png",
              97:"icons/yo.jpg",
              98:"icons/pedro.jpg",
              99:"icons/success.png"}

def get_event(ind):
    if ind in ind_recompensa:
        return "Recompensa"
    elif ind in ind_castigo:
        return "Castigo"
    elif ind == 99:
        return "Premio"

    return "Reto"
