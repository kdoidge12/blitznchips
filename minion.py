from __future__ import print_function
import pygame
from pygame.locals import *
import sys
import constants
#from map import Map

class Minions():
	def __init__(self, object):
		self.level = constants.minions[object.level]['level']
		self.name = constants.minions[object.level]['name']
		self.image = constants.minions[object.level]['image']
		self.HP = constants.minions[object.level]['hp']
		self.speed = constants.minions[object.level]['move']
		self.movingX = object.xlist[6]
		self.movingY = object.ylist[3]


class Bullet():
	def __init__(self,y=0,x=0,dam=0):
		self.mX = x
		self.mY = y  
		self.damage = dam

	def move(self,x):
		self.setmX(self.mX - x)

	def setmX(self,x):
		self.mX = x

	def setmY(self,y):
		self.mY = y
