from __future__ import print_function
import pygame
from pygame.locals import *
import sys
import consats
import tower

#39,31
#reads in the command line argv for the map text file

pygame.init()

##################################################
#These lines test the current screen size and    #
#then pick a appropriate window size for the game#
##################################################
infoObject = pygame.display.Info()
if(infoObject.current_w >=1920):
	screenWidth = 1000
else:
	screenWidth = 800

if(infoObject.current_h >= 952):
	screenHeight = 800
else:
	screenHeight = 640



#size is width x heigth of the window that opens#
size = (screenWidth,screenHeight)
windowSurface = pygame.display.set_mode((size),0,32)
pygame.display.set_caption('Map Test')

#these are the width and height of the game tiles
width =  screenWidth / 40
height = screenHeight /32
screenTileW = screenWidth / width
screenTileH = screenHeight / height


####################################################
#These funcs are just to help with making a list of# 
#numebr by the width and height. X is a input and  #
#is the multiply to generate the numbers           #
####################################################
def multi25W(x):
	return x * width

def multi25H(x):
	return x * height  


###################################################
#makes to list one for the width and the other for# 
#the height ex.[0,25,50,....]. xlist and ylist are#
#a list of all the possiable pixal grid values    #
###################################################
def makeListWH(w,h):
	xl = map(multi25W,range(0,w))
	yl = map(multi25H,range(0,h))
	return xl, yl


###################################################
#this read the file and makes it into  a 		  #
#list of list. Where f is a file that will contain#
#the map information. grid will be the main game  #
#grid in which everything will be saved to        #
###################################################
def popGrid(f):
	g = []
	row = 0
	for xy in (f):
		g.append([])
		for dxdy in xy:
			g[row].append(dxdy)
		row = row+1
	return g


###################################################
#This Func take in a populated gird and draws it  #
#to the screen. Will loop through all of the grid #
#and then draw and color code where needed also   #
#calls the draw button func to draw the buttons   #
###################################################
def drawMap(g):
	x = 0
	y = 0 
	margin = 0
	for row in g:
		#End everyline, including last line of map with '/n' but only need to do it once
		if not row:
			row.pop()
		for column in row:
			if(column is "0"):
				image = consats.GRASS
			if(column == "1"):
				image = consats.SPACE
			if(column == "2"):
				image = consats.WALL
			if(column == "3"):
				image = consats.SPACE
			if(column == "4"):
				image = consats.WALL
			if(column == "5"):
				image = consats.REDTOWER
			if(column == "6"):
				image = consats.BLUETOWER
			
			windowSurface.blit(image,(x,y))
			#pygame.draw.rect(windowSurface,color,(x,y,width,height),0)
			x = x + height + margin
		y=y+width + margin
		x = 0
		pygame.display.update()
	tower.drawButtons()	


##########################################
#Draw the grid in line onto the playable #
#map surface. ONLY draw to playable areas#
##########################################
def drawGrid(g):
	x = width
	y = height
	z = ylist[25]
	a = width
	b = height
	c = xlist[39]
	glen = len(g)-7
	#print(glen)
	#for row in range(glen):
	row = 0
	rlen = len(g[row])-2
	#print(rlen)
	for col in range(rlen):
		#vertical lines
		pygame.draw.lines(windowSurface,consats.WHITE,False,[(x,y),(x,z)],3) 
		x=x+width
	for x in range(glen):
		#horizontal lines
		pygame.draw.lines(windowSurface,consats.WHITE,False,[(a,b),(c,b)],3)
		b=b+height
	pygame.display.update()

########################################################
#x and y are pixel postion on windowsurface check where#
#these values are and returns an order pair base on x,y#
########################################################
def getGridCord(x,y):
	i = 0
	j = 1
	pair = []
	while(i < len(xlist)):
		if(xlist[i] <= x and x < xlist[j]):
			pair.append(i)
			break
		
		i = i + 1
		j = j + 1
	a = 0
	b = 1
	while(a < len(ylist)):
		if(ylist[a] <= y and y < ylist[b]):
			pair.append(a)
			#print(pair)
			break
		a = a + 1
		b = b + 1

	return pair

#setup
#x,y,x2,y2
xlist, ylist = makeListWH(screenTileW+1,screenTileH+1)

exbutton = [xlist[1],ylist[27],width*3+xlist[1],height*2+ylist[27]]
exbutton2 = [xlist[6],ylist[27],width*3+xlist[6],height*2+ylist[27]]