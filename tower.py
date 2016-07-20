from __future__ import print_function
import pygame
from pygame.locals import *
import sys
import map

###################################################
#The func test whether a tower can be put here    #
#Buy taking in a x and y int and checking the grid#
###################################################
def canPutTower(x,y,g):
	if(g[y][x] is '0'):
		return True
	else:
		return False


##########################################
#draws all buttons onto the map          #
##########################################
def drawButtons():
	drawRedButton(0)
	drawBlueButton(0)


##########################################
#just draws Example button x is on or off#
##########################################
def drawRedButton(x):
	if(x is 0):
		exam = pygame.image.load("ex2.jpg")
		map.windowSurface.blit(exam,(map.exbutton[0],map.exbutton[1]))
	else:
		exam = pygame.image.load("ex.jpg")
		map.windowSurface.blit(exam,(map.exbutton[0],map.exbutton[1]))
	pygame.display.update()


###########################################
#just draws Example2 button x is on or off#
###########################################
def drawBlueButton(x):
		if(x is 0):
			exam2 = pygame.image.load("ex2.jpg")
			map.windowSurface.blit(exam2,(map.exbutton2[0],map.exbutton2[1]))
		else:
			exam2 = pygame.image.load("ex.jpg")
			map.windowSurface.blit(exam2,(map.exbutton2[0],map.exbutton2[1]))
		pygame.display.update()