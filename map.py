from __future__ import print_function
import pygame
from pygame.locals import *
import sys
import constants
from minion import Bullet
#write a function that will return the current updated map in blit form

class Map:
	def multi(self, x,y):
		coordinate = self.getGridCord(x,y)
		if(self.grid[coordinate[1]][coordinate[0]] == "9" or self.grid[coordinate[1]][coordinate[0]] == "8"):
			return -1
		else:
			return 1
	def change(self,x,y):
		coordinate = self.getGridCord(x,y)
		if(self.grid[coordinate[1]][coordinate[0]] == "7" or self.grid[coordinate[1]][coordinate[0]] == "8"):
			return True
		else:
			return False

	def blit_update(self):
		pygame.display.update()
		pygame.time.delay(100)

	def moveX(self,minions):
		self.windowSurface.blit(self.filler,(0,0))
		for x in minions:
			mul = self.multi(x.movingX,x.movingY)
			if(self.change(x.movingX,x.movingY)):
				self.windowSurface.blit(constants.man,(x.movingX,x.movingY))
				x.movingY = x.movingY + (25*mul)
			else:
				self.windowSurface.blit(constants.man,(x.movingX,x.movingY))
				x.movingX = x.movingX + (25*mul)
			#pygame.display.update()
		pygame.display.update()
		pygame.time.delay(100)

	def multi25W(self,x):
		return x * self.width

####################################################
#These funcs are just to help with making a list of#
#numebr by the width and height. X is a input and  #
#is the multiply to generate the numbers           #
####################################################
	def multi25H(self,x):
		return x * self.height

###################################################
#makes to list one for the width and the other for#
#the height ex.[0,25,50,....]. xlist and ylist are#
#a list of all the possiable pixal grid values    #
###################################################
	def makeListWH(self,w,h):
		xl = map(self.multi25W,range(0,w))
		yl = map(self.multi25H,range(0,h))
		return xl,yl

###################################################
#this read the file and makes it into  a 		  #
#list of list. Where f is a file that will contain#
#the map information. grid will be the main game  #
#grid in which everything will be saved to        #
###################################################
	def popGrid(self,f):
		row = 0
		for xy in (f):
			self.grid.append([])
			for dxdy in xy:
				self.grid[row].append(dxdy)
			row = row + 1


###################################################
#This Func take in a populated gird and draws it  #
#to the screen. Will loop through all of the grid #
#and then draw and color code where needed also   #
#calls the draw button func to draw the buttons   #
###################################################
	def drawMap(self):
		x = 0
		y = 0
		margin = 0
		for row in self.grid:
			if not row:
				row.pop()
			for column in row:
				if(column is "0"):
					image = constants.GRASS
				if(column == "1"):
					image = constants.SPACE
				if(column == "2"):
					image = constants.WALL
				if(column == "3" or column == "7" or column is "8" or column is "9"):
					image = constants.SPACE
				if(column == "4"):
					image = constants.WALL
				if(column == "5"):
					image = constants.REDTOWER
				if(column == "6"):
					image = constants.BLUETOWER

				self.windowSurface.blit(image,(x,y))
				x = x + self.height + margin
			y=y+self.width + margin
			x = 0

		self.drawButtons()
		pygame.display.update()
		self.filler = pygame.Surface.copy(self.windowSurface)



##########################################
#Draw the grid in line onto the playable #
#map surface. ONLY draw to playable areas#
##########################################
	def drawGrid(self):
		x = self.width
		y = self.height
		z = self.ylist[25]
		a = self.width
		b = self.height
		c = self.xlist[39]
		glen = len(self.grid)-7
		#print(glen)
		#for row in range(glen):
		row = 0
		rlen = len(self.grid[row])-2
		#print(rlen)
		for col in range(rlen):
			#vertical lines
			pygame.draw.lines(self.windowSurface,constants.WHITE,False,[(x,y),(x,z)],3)
			x=x+self.width
		for x in range(glen):
			#horizontal lines
			pygame.draw.lines(self.windowSurface,constants.WHITE,False,[(a,b),(c,b)],3)
			b=b+self.height


		pygame.display.update()

	def drawRange(self,ta):
		for x in ta:
			pygame.draw.circle(self.windowSurface,constants.RED,[x.centerx,x.centery],x.radius,1)
		pygame.display.update()

########################################################
#x and y are pixel postion on windowsurface check where#
#these values are and returns an order pair base on x,y#
########################################################
	def getGridCord(self,x,y):
		i = 0
		j = 1
		pair = []
		while(i < len(self.xlist)):
			if(self.xlist[i] <= x and x <self.xlist[j]):
				pair.append(i)
				break

			i = i + 1
			j = j + 1
		a = 0
		b = 1
		while(a < len(self.ylist)):
			if(self.ylist[a] <= y and y < self.ylist[b]):
				pair.append(a)
				#print(pair)
				break
			a = a + 1
			b = b + 1

		return pair


	###################################################
	#The func test whether a tower can be put here    #
	#Buy taking in a x and y int and checking the grid#
	###################################################
	def canPutTower(self,x,y):
		if(self.grid[y][x] is '0'):
			return True
		else:
			return False


	##########################################
	#draws all buttons onto the map          #
	##########################################
	def drawButtons(self):
		self.drawRedButton(0)
		self.drawBlueButton(0)


	##########################################
	#just draws Example button x is on or off#
	##########################################
	def drawRedButton(self,x):
		if(x is 0):
			exam = pygame.image.load("ex2.jpg")
			self.windowSurface.blit(exam,(self.exbutton[0],self.exbutton[1]))
		else:
			exam = pygame.image.load("ex.jpg")
			self.windowSurface.blit(exam,(self.exbutton[0],self.exbutton[1]))
		#pygame.display.update()


	###########################################
	#just draws Example2 button x is on or off#
	###########################################
	def drawBlueButton(self,x):
			if(x is 0):
				exam2 = pygame.image.load("ex2.jpg")
				self.windowSurface.blit(exam2,(self.exbutton2[0],self.exbutton2[1]))
			else:
				exam2 = pygame.image.load("ex.jpg")
				self.windowSurface.blit(exam2,(self.exbutton2[0],self.exbutton2[1]))
			#pygame.display.update()

	def bulletShoot(self,x):
		#print("BulletShoot")
		mybull = Bullet(x.centerx,x.centery,x.dam)
		self.bullets.append(mybull)
	#while thing == 1:
		for b in self.bullets:
			#print("Bullet",b.mX,b.mY)
			b.move(10)

		for bullet in self.bullets:
			if(bullet.mX < 0):
				self.bullets.remove(bullet)

		self.windowSurface.blit(self.filler,(0,0))

		for bullet in self.bullets:
			self.windowSurface.blit(constants.BULLET,pygame.Rect(bullet.mY,bullet.mX,0,0))

		pygame.display.flip()
		pygame.time.delay(100)





	def __init__(self,grid):
		pygame.init()
		infoObject = pygame.display.Info()
		#print(infoObject)
		##################################################
		#These lines test the current screen size and    #
		#then pick a appropriate window size for the game#
		##################################################
		if(infoObject.current_w >=1920):
			self.screenWidth = 1000
		else:
			self.screenWidth = 800

		if(infoObject.current_h >= 950):
			self.screenHeight = 800
		else:
			self.screenHeight = 640

		self.level = 1
		self.bullets = []
		self.grid = [] # Creates empty list to hold Game Grid
		self.size = (self.screenWidth,self.screenHeight)
		self.windowSurface = pygame.display.set_mode((self.size),0,32)
		pygame.display.set_caption('Map Test')
		self.width =  self.screenWidth / 40
		self.height = self.screenHeight /32
		self.screenTileW = self.screenWidth / self.width
		self.screenTileH = self.screenHeight / self.height
		self.xlist, self.ylist = self.makeListWH(self.screenTileW+1,self.screenTileH+1)
		self.exbutton = [self.xlist[1],self.ylist[27],self.width*3+self.xlist[1],self.height*2+self.ylist[27]]
		self.exbutton2 = [self.xlist[6],self.ylist[27],self.width*3+self.xlist[6],self.height*2+self.ylist[27]]
