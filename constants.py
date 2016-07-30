from __future__ import print_function
import pygame
from pygame.locals import *
import sys

#const color with the RGB values
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,200)
B_BLUE = (0,0,255)
WHITE = (255,255,255)
GRAY = (100,100,100)
YELLOW = (255,255,0)
BLACK = (0,0,0)
RICK_GREEN = (20, 184, 87)
RICK_PURPLE = (78, 11, 74)

man = pygame.image.load("sim.png")

REDTOWER = pygame.image.load("r.jpg")
BLUETOWER = pygame.image.load("b.jpg")
GRASS = pygame.image.load("grass.jpg")
WALL = pygame.image.load("wall.jpg")
SPACE = pygame.image.load("space.jpg")
BULLET = pygame.image.load("sim.png")
#Minion Info
#minions = [[Level,name, 'imagefile', HP, Move_Speed],....]
minions = [{'level': 1,'name': "A", 'image': 'clg.png', 'hp': 10, 'move' : 10, 'score': 100, 'value': 5},
		   {'level': 2,'name': "B", 'image': 'clg.png', 'hp': 18, 'move' : 10, 'score': 135, 'value': 8},
		   {'level': 3,'name': "C", 'image': 'clg.png', 'hp': 32, 'move' : 10, 'score': 180, 'value': 14}]
