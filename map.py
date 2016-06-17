from __future__ import print_function
import pygame
from pygame.locals import *
import sys


#const color with the RGB values
red = (255,0,0)
green = (0,255,0)
blue = (0,0,200)
bright_blue = (0,0,255)
white = (255,255,255)
gray = (100,100,100)
yellow = (255,255,0)
black = (0,0,0)


pygame.init()
infoObject = pygame.display.Info()
print(infoObject.current_w)
print(infoObject.current_h)
if(infoObject.current_w >=1920):
	screenWidth = 1000
else:
	screenWidth = 800

if(infoObject.current_h >= 952):
	screenHeight = 800
else:
	screenHeight = 640

#size is width x heigth of the window that opens
size = (screenWidth,screenHeight)
windowSurface = pygame.display.set_mode((size),0,32)
pygame.display.set_caption('Map Test')

#these are the width and height of the game tiles
width =  screenWidth / 40
height = screenHeight /32
screenTileW = screenWidth / width
screenTileH = screenHeight / height


#These fucn are just to help with making a list of numebr by the width and height	
def multi25W(x):
	return x * width

def multi25H(x):
	return x * height  

#makes to list one for the width and the other for the height ex.[0,25,50,....]
def makeListWH(w,h):
	xlist = map(multi25W,range(0,w))
	ylist = map(multi25H,range(0,h))
	return xlist, ylist


#this read the file and makes it into  a list of list 
def popGrid(f):
	grid = []
	row = 0
	for xy in (f):
		grid.append([])
		for dxdy in xy:
			grid[row].append(dxdy)
		row = row+1
	return grid

#this reads the grid and draw the map based on the given color
def drawMap(grid):
	x = 0
	y = 0 
	margin = 0
	for row in grid:
		#End everyline, including last line of map with '/n' but  only need to do it once
		if not row:
			row.pop()
		for column in row:
			if(column is "0"):
				color = green
			if(column == "1"):
				color = red
			if(column == "2"):
				color = blue
			if(column == "3"):
				color = white
			if(column == "4"):
				color = gray
			if(column == "5"):
				color = yellow
			if(column == "6"):
				color = black
			pygame.draw.rect(windowSurface,color,(x,y,width,height),0)
			x = x + height + margin
		y=y+width + margin
		x = 0
	drawButtons()	

#draws the grid onto the map 	
def drawGrid():
	x = width
	y = height
	z = ylist[25]
	a = width
	b = height
	c = xlist[39]
	glen = len(grid)-7
	#print(glen)
	#for row in range(glen):
	row = 0
	rlen = len(grid[row])-2
	#print(rlen)
	for col in range(rlen):
		#vertical lines
		pygame.draw.lines(windowSurface,white,False,[(x,y),(x,z)],3) 
		x=x+width
	for x in range(glen):
		#horizontal lines
		pygame.draw.lines(windowSurface,white,False,[(a,b),(c,b)],3)
		b=b+height


#take mouse up click and gives back a pair of x,y cord
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


def canPutTower(x,y):
	if(grid[y][x] is '0'):
		return True
	else:
		return False



######################################################################################
#39,31
#reads in the command line argv for the map text file
f = file(sys.argv[1],'r')

#x,y,x2,y2
xlist, ylist = makeListWH(screenTileW+1,screenTileH+1)


exbutton = [xlist[1],ylist[27],width*3+xlist[1],height*2+ylist[27]]
exbutton2 =[xlist[6],ylist[27],width*3+xlist[6],height*2+ylist[27]]


def drawButtons():
		drawExample(0)
		drawExample2(0)

def drawExample(x):
		#print(x)
		if(x is 0):
			exam = pygame.image.load("ex2.jpg")
			windowSurface.blit(exam,(exbutton[0],exbutton[1]))
		else:
			exam = pygame.image.load("ex.jpg")
			windowSurface.blit(exam,(exbutton[0],exbutton[1]))
		pygame.display.update()
	
def drawExample2(x):
		#print(x)
		if(x is 0):
			exam2 = pygame.image.load("ex2.jpg")
			windowSurface.blit(exam2,(exbutton2[0],exbutton2[1]))
		else:
			exam2 = pygame.image.load("ex.jpg")
			windowSurface.blit(exam2,(exbutton2[0],exbutton2[1]))
		pygame.display.update()


# draw the window onto the screen
grid = popGrid(f)
drawMap(grid)

pygame.display.update()
exswitch = False
exswitch2 = False
# run the game loop
while True:
	gswitch = pygame.key.get_pressed()[K_g]
	cswitch = pygame.key.get_pressed()[K_c]
	if(gswitch == 1):
		drawGrid()
		pygame.display.flip()
	if(cswitch == 1):
		drawMap(grid)
		pygame.display.update()
	
	for event in pygame.event.get():

		if(exswitch is True and event.type is pygame.MOUSEBUTTONDOWN):
			mousex, mousey = pygame.mouse.get_pos()
			cord = getGridCord(mousex,mousey)
			if (canPutTower(cord[0],cord[1]) is True):
				pygame.draw.rect(windowSurface,yellow,(xlist[cord[0]],xlist[cord[1]],width,height),0)
				grid[cord[1]][cord[0]] = '5'
			exswitch = False
			pygame.display.update()

		if(exswitch2 is True and event.type is pygame.MOUSEBUTTONDOWN):
			mousex, mousey = pygame.mouse.get_pos()
			cord = getGridCord(mousex,mousey)
			if (canPutTower(cord[0],cord[1]) is True):
				pygame.draw.rect(windowSurface,black,(xlist[cord[0]],xlist[cord[1]],width,height),0)
				grid[cord[1]][cord[0]] = '6'
			exswitch2 = False
			pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			mousex, mousey = pygame.mouse.get_pos()
			cord = getGridCord(mousex,mousey)
			if((exbutton[0] <= xlist[cord[0]] and xlist[cord[0]] < exbutton[2]) and (exbutton[1] <= ylist[cord[1]] and ylist[cord[1]] < exbutton[3])):
				drawExample(1)
				exswitch = True

			elif((exbutton2[0] <= xlist[cord[0]] and xlist[cord[0]] < exbutton2[2]) and (exbutton2[1] <= ylist[cord[1]] and ylist[cord[1]] < exbutton2[3])):
				drawExample2(1)
				exswitch2 = True
			else:
				drawExample(0)
				exswitch2 = False
				drawExample2(0)
				exswitch = False

		if event.type == QUIT:
			pygame.quit()
	    		sys.exit()
	


