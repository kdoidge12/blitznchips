from __future__ import print_function
import pygame
from pygame.locals import *
import sys
import constants
from minion import Bullet
#write a function that will return the current updated map in blit form

class FontTemplate:
    def __init__(self, fontype_size):
        self.font_pair = ()
        fontFullFileName = pygame.font.match_font(fontype_size[0])
        self.font_pair = pygame.font.Font(fontFullFileName, fontype_size[1])

    def Draw(self, surface, fontName, size, text, rectOrPosToDrawTo, color,
            alignHoriz='left', alignVert='top', antialias=False):
        pair = (fontName, size)
        fontSurface = self.font_pair.render(text, antialias, color)
        if isinstance(rectOrPosToDrawTo, tuple):
            surface.blit(fontSurface, rectOrPosToDrawTo)
        elif isinstance(rectOrPosToDrawTo, pygame.Rect):
            fontRect = fontSurface.get_rect()
            # align horiz
            if alignHoriz == 'center':
                fontRect.centerx = rectOrPosToDrawTo.centerx
            elif alignHoriz == 'right':
                fontRect.right = rectOrPosToDrawTo.right
            else:
                fontRect.x = rectOrPosToDrawTo.x  # left
            # align vert
            if alignVert == 'center':
                fontRect.centery = rectOrPosToDrawTo.centery
            elif alignVert == 'bottom':
                fontRect.bottom = rectOrPosToDrawTo.bottom
            else:
                fontRect.y = rectOrPosToDrawTo.y  # top

            surface.blit(fontSurface, fontRect)

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

	def live_check(self,minions,x):
		coordinate = self.getGridCord(x.movingX,x.movingY)
		if(self.grid[coordinate[1]][coordinate[0]] == "B"):
			minions.remove(x)
			self.lives = self.lives - 1

	def blit_update(self):
		pygame.display.update()
		pygame.time.delay(100)

	def moveX(self,minions):
		if self.width == 20:
			pixels = 20
		else:
			pixels = 25
		self.windowSurface.blit(self.filler,(0,0))
		for x in minions:
			mul = self.multi(x.movingX,x.movingY)
			if(self.change(x.movingX,x.movingY)):
				self.windowSurface.blit(constants.man,(x.movingX,x.movingY))
				x.movingY = x.movingY + (pixels*mul)
			else:
				self.windowSurface.blit(constants.man,(x.movingX,x.movingY))
				x.movingX = x.movingX + (pixels*mul)
			self.live_check(minions, x)


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
			if(self.startx is 0):
				self.startx = int(xy[0])
				self.starty = int(xy[1])
			else:
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
		for row in self.grid:
			if not row:
				row.pop()
			for column in row:
				if(column is "0"):
					image = constants.GRASS
					self.windowSurface.blit(image,(x,y))
				if(column == "1"):
					image = constants.SPACE
					self.windowSurface.blit(image,(x,y))
				if(column == "2"):
					image = constants.WALL
					self.windowSurface.blit(image,(x,y))
				if(column == "3" or column == "7" or column is "8" or column is "9" or column is "B"):
					image = constants.SPACE
					self.windowSurface.blit(image,(x,y))
				if(column == "4"):
					image = constants.WALL
					self.windowSurface.blit(image,(x,y))
				if(column == "5"):
					image = constants.REDTOWER
					self.windowSurface.blit(image,(x,y))
				if(column == "6"):
					image = constants.BLUETOWER
					self.windowSurface.blit(image,(x,y))
				if(column == "A"):
					pass
					#image = constants.BLANK


				x = x + self.height
			y=y+self.width
			x = 0
		rect = pygame.Rect(self.xlist[1], self.ylist[1], self.width * 38, self.height * 24)
		pygame.draw.rect(self.windowSurface, constants.WHITE, rect, 3)
		self.drawMenu()
		self.drawStats()
		self.drawButtons()
		pygame.display.update()
		self.filler = pygame.Surface.copy(self.windowSurface)
		self.updateMoney()
		self.updateScore()
		self.updateLives()



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
    #draws all static font on the map        #
    ##########################################
	def drawMenu(self):
		y = self.screenHeight - (self.height * 26)
		fonts = FontTemplate(('arial', 15))
		rect = pygame.Rect(self.width, self.height * 25, self.width *38, y)
		pygame.draw.rect(self.windowSurface, constants.BLACK, rect)
		pygame.draw.rect(self.windowSurface, constants.WHITE, rect, 3)
		fonts.Draw(self.windowSurface, 'arial', 15, 'TOWERS', (self.width * 2, ((self.height * 25) + self.width / 2) ), constants.WHITE, 'left', 'center', True)
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, 'LEVEL', (self.xlist[2], self.ylist[29]), constants.WHITE, 'left', 'center', True)
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, 'LIVES', (self.xlist[9], self.ylist[29]), constants.WHITE, 'center', 'center', True)
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, 'SCORE', (self.xlist[15], self.ylist[29]), constants.WHITE, 'center', 'center', True)
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, 'MONEY', (self.xlist[21], self.ylist[29]), constants.WHITE, 'center', 'center', True)
		rect = pygame.Rect(self.xlist[27], self.ylist[26], self.width * 11, self.height * 4 )
		pygame.draw.rect(self.windowSurface, constants.WHITE, rect, 2)

	def drawTowerInfo(self, type):
		if type == 1:
			damage = '1'
			radius = '75'
			cost = '25'
			speed = 'Medium'
		elif type == 2:
			damage = '10'
			radius = '150'
			cost = '75'
			speed = 'Fast'
		fonts = FontTemplate(('arial', 12))
		fonts.Draw(self.windowSurface, 'arial', 12, 'DAMAGE: ' + damage, (self.xlist[29], self.ylist[26]), constants.WHITE, 'center', 'center', True)
		fonts = FontTemplate(('arial', 12))
		fonts.Draw(self.windowSurface, 'arial', 12, 'RADIUS: ' + radius, (self.xlist[29], self.ylist[27]), constants.WHITE, 'center', 'center', True)
		fonts = FontTemplate(('arial', 12))
		fonts.Draw(self.windowSurface, 'arial', 12, 'COST: ' + cost, (self.xlist[29], self.ylist[28]), constants.WHITE, 'center', 'center', True)
		fonts = FontTemplate(('arial', 12))
		fonts.Draw(self.windowSurface, 'arial', 12, 'SPEED: ' + speed, (self.xlist[29], self.ylist[29]), constants.WHITE, 'center', 'center', True)
		pygame.display.update()

	def drawStats(self):
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, str(" "), (self.xlist[12], self.ylist[29]), constants.WHITE, 'center', 'center', True)
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, str(" "), (self.xlist[18], self.ylist[29]), constants.WHITE, 'center', 'center', True)
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, str(" "), (self.xlist[24], self.ylist[29]), constants.WHITE, 'center', 'center', True)

    ##########################################
    #pass in money to update money on menu   #
    ##########################################
	def updateMoney(self):
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, str(self.money), (self.xlist[24], self.ylist[29]), constants.WHITE, 'center', 'center', True)
		pygame.display.update()

    ##########################################
    #pass in money to update money on menu   #
    ##########################################
	def updateLevel(self):
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, str(self.level), (self.xlist[2], self.ylist[30]), constants.WHITE, 'center', 'center', True)
		pygame.display.update()


	##########################################
	#pass in lives to update lives on menu   #
	##########################################
	def updateLives(self):
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, str(self.lives), (self.xlist[12], self.ylist[29]), constants.WHITE, 'center', 'center', True)
		pygame.display.update()

	##########################################
	#pass in score to update score on menu   #
	##########################################
	def updateScore(self):
		fonts = FontTemplate(('arial', 15))
		fonts.Draw(self.windowSurface, 'arial', 15, str(self.score), (self.xlist[18], self.ylist[29]), constants.WHITE, 'center', 'center', True)
		pygame.display.update()

	##########################################
	#draws all buttons onto the map          #
	##########################################
	def drawButtons(self):
		self.drawRedButton(0)
		self.drawBlueButton(0)
		self.drawStartButton(0)
		self.drawHelpButton(0)
		self.drawReturnButton(0)

	##########################################
	#just draws start button x is on or off#
	##########################################
	def drawStartButton(self, x):
		fonts = FontTemplate(('arial', 15))
		rect = pygame.Rect(self.startbutton[0], self.startbutton[1], self.width*4+self.xlist[1], self.height*2)
		if(x is 0):
			pygame.draw.rect(self.windowSurface, constants.BLACK, rect)
			pygame.draw.rect(self.windowSurface, constants.WHITE, rect, 3)
			fonts.Draw(self.windowSurface, 'arial', 15, 'START', rect, constants.WHITE, 'center', 'center', True)
		else:
			pygame.draw.rect(self.windowSurface, constants.RICK_GREEN, rect)
			pygame.draw.rect(self.windowSurface, constants.WHITE, rect, 3)
			fonts.Draw(self.windowSurface, 'arial', 15, 'START', rect, constants.WHITE, 'center', 'center', True)


	##########################################
	#just draws mainmenu button x is on or off#
	##########################################
	def drawReturnButton(self, x):
		fonts = FontTemplate(('arial', 15))
		rect = pygame.Rect(self.returnbutton[0], self.returnbutton[1], self.width*4+self.xlist[1], self.height*2)
		if(x is 0):
			pygame.draw.rect(self.windowSurface, constants.BLACK, rect)
			pygame.draw.rect(self.windowSurface, constants.WHITE, rect, 3)
			fonts.Draw(self.windowSurface, 'arial', 15, 'MAIN MENU', rect, constants.WHITE, 'center', 'center', True)
		else:
			pygame.draw.rect(self.windowSurface, constants.RICK_GREEN, rect)
			pygame.draw.rect(self.windowSurface, constants.WHITE, rect, 3)
			fonts.Draw(self.windowSurface, 'arial', 15, 'MAIN MENU', rect, constants.WHITE, 'center', 'center', True)


	##########################################
	#just draws mainmenu button x is on or off#
	##########################################
	def popupWindow(self, text):
		x = self.screenWidth / 3
		fonts = FontTemplate(('arial', 18))
		rect = pygame.Rect(x, self.ylist[12], x, 3 * self.height)
		pygame.draw.rect(self.windowSurface, constants.BLACK, rect)
		pygame.draw.rect(self.windowSurface, constants.WHITE, rect, 3)
		fonts.Draw(self.windowSurface, 'arial', 18, text, rect, constants.WHITE, 'center', 'center', True)
		pygame.display.flip()

	##########################################
	#just draws help button x is on or off#
	##########################################
	def drawHelpButton(self, x):
		fonts = FontTemplate(('arial', 15))
		rect = pygame.Rect(self.helpbutton[0], self.helpbutton[1], self.width*4+self.xlist[1], self.height*2)
		if(x is 0):
			pygame.draw.rect(self.windowSurface, constants.BLACK, rect)
			pygame.draw.rect(self.windowSurface, constants.WHITE, rect, 3)
			fonts.Draw(self.windowSurface, 'arial', 15, 'HELP', rect, constants.WHITE, 'center', 'center', True)
		else:
			pygame.draw.rect(self.windowSurface, constants.RICK_GREEN, rect)
			pygame.draw.rect(self.windowSurface, constants.WHITE, rect, 3)
			fonts.Draw(self.windowSurface, 'arial', 15, 'HELP', rect, constants.WHITE, 'center', 'center', True)


	##########################################
	#just draws Example button x is on or off#
	##########################################
	def drawRedButton(self,x):
		if(x is 0):
			exam = pygame.image.load("tower1.png")
			self.windowSurface.blit(exam,(self.exbutton[0],self.exbutton[1]))
		else:
			exam = pygame.image.load("tower1.png")
			self.windowSurface.blit(exam,(self.exbutton[0],self.exbutton[1]))
		#pygame.display.update()


	###########################################
	#just draws Example2 button x is on or off#
	###########################################
	def drawBlueButton(self,x):
			if(x is 0):
				exam2 = pygame.image.load("tower2.png")
				self.windowSurface.blit(exam2,(self.exbutton2[0],self.exbutton2[1]))
			else:
				exam2 = pygame.image.load("tower2.png")
				self.windowSurface.blit(exam2,(self.exbutton2[0],self.exbutton2[1]))
			#pygame.display.update()

	def bulletShoot(self,mini,tow):
		totalX = (mini.movingX - tow.centerx)/2
		totalY = (mini.movingY - tow.centery)/2
		mybull = Bullet(tow.centerx,tow.centery,tow.dam)
		myrect = pygame.draw.rect(self.windowSurface,tow.color,(mybull.mY,mybull.mX,tow.sizex,tow.sizey))
		myrect = myrect.move(totalX,totalY)
		myrect = pygame.draw.rect(self.windowSurface,tow.color,myrect)
		myrect = myrect.move(totalX,totalY)
		myrect = pygame.draw.rect(self.windowSurface,tow.color,myrect)

	def __init__(self,grid, money, score, lives):
		pygame.init()
		infoObject = pygame.display.Info()
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

		self.startx = 0
		self.starty =0
		self.pbullet =[]
		self.money = money
		self.score = score
		self.lives = lives
		self.level = 0
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
		self.exbutton = [self.xlist[2],self.ylist[27],self.width+self.xlist[2],self.height+self.ylist[27]]
		self.exbutton2 = [self.xlist[5],self.ylist[27],self.width*2+self.xlist[5],self.height*2+self.ylist[27]]
		self.startbutton = [self.xlist[9],self.ylist[26],self.width*5+self.xlist[9],self.height*2+self.ylist[26]]
		self.helpbutton = [self.xlist[15],self.ylist[26],self.width*5+self.xlist[15],self.height*2+self.ylist[26]]
		self.returnbutton = [self.xlist[21],self.ylist[26],self.width*5+self.xlist[21],self.height*2+self.ylist[26]]
		self.bool = False
