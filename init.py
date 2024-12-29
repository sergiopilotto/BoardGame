import pygame
import random
from colors import *
from screen import *
from squads import *
### INIT


nb_squads = 4
Squads = {}
for i in range(nb_squads):
    Squads["S" + str(i + 1)] = Squad("Equipo " + str(i + 1), i)
