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

REDTOWER = pygame.image.load("mortyt.png")
BLUETOWER = pygame.image.load("rickt.png")
GRASS = pygame.image.load("grass.jpg")
WALL = pygame.image.load("wall.jpg")
SPACE = pygame.image.load("space.jpg")
BULLET = pygame.image.load("sim.png")
#Minion Info
#minions = [[Level,name, 'imagefile', HP, Move_Speed],....]
minions = [{'level': 1,'name': "A", 'image': 'clg.png', 'hp': 10, 'move' : 10, 'score': 100, 'value': 5},
		   {'level': 2,'name': "B", 'image': 'clg.png', 'hp': 18, 'move' : 10, 'score': 135, 'value': 8},
		   {'level': 3,'name': "C", 'image': 'clg.png', 'hp': 32, 'move' : 10, 'score': 180, 'value': 12},
		   {'level': 4,'name': "C", 'image': 'clg.png', 'hp': 50, 'move' : 10, 'score': 180, 'value': 17},
		   {'level': 5,'name': "C", 'image': 'clg.png', 'hp': 80, 'move' : 10, 'score': 180, 'value': 23},
		   {'level': 6,'name': "C", 'image': 'clg.png', 'hp': 120, 'move' : 10, 'score': 180, 'value': 30},
		   {'level': 7,'name': "C", 'image': 'clg.png', 'hp': 165, 'move' : 10, 'score': 180, 'value': 38},
		   {'level': 8,'name': "C", 'image': 'clg.png', 'hp': 220, 'move' : 10, 'score': 180, 'value': 47},
		   {'level': 9,'name': "C", 'image': 'clg.png', 'hp': 290, 'move' : 10, 'score': 180, 'value': 57},
		   {'level': 10,'name': "C", 'image': 'clg.png', 'hp': 390, 'move' : 10, 'score': 180, 'value': 70}]
