from __future__ import print_function
import pygame
from pygame.locals import *
import sys
from map import Map


class Tower(Map):
	def __init__(self,typ=0,tly=0,tlx=0):
		self.ttype = typ
		self.centerx = self.setCenter(tlx)
		self.centery = self.setCenter(tly)
		self.dam = 0
		self.radius = 0
		self.setType()
		
	def setType(self):
		if(self.ttype is 1 ):
			self.dam = 1
			self.radius = 75

		if(self.ttype is 2):
			self.dam = 10
			self.radius = 150

	def setCenter(self,num):
		x = (num + (self.ttype * 25) + num)/2
		return x

	def pingTower(self,mini):
		#print("Center x,y",self.centerx,self.centery,self.radius)
		rb = self.radius + self.centerx
		lb = self.centerx - self.radius
		ub = self.radius + self.centery
		lob = self.centery - self.radius
		#print(rb,lb,ub,lob)
		x = mini.movingX
		y = mini.movingY
		#print(x,y)
		if((lb <= x and x <= rb)and(lob <= y and y <= ub)):
			#print("Found it")
			return True
		else:
			return False

	def damMini(self,x):
		x.HP = x.HP - self.dam
		if(x.HP <= 0):
			return True
		else:
			return False


		


