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
ind_castigo = [10, 29, 39, 53, 62, 73, 77, 83, 88, 92]

def get_event(ind):
    if ind in ind_recompensa:
        return "Recompensa"
    elif ind in ind_castigo:
        return "Castigo"
    elif ind == 99:
        return "Premio"

    return "Reto"
