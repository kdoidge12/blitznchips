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

man = pygame.image.load("rick.png")
clock = pygame.time.Clock()
speedX=0

xlist, ylist = makeListWH(screenTileW+1,screenTileH+1)
exbutton = [xlist[1],ylist[27],width*3+xlist[1],height*2+ylist[27]]
movingX = xlist[6]
movingY = ylist[3]

pygame.init()

#size is width x heigth of the window that opens
size = (1000,800)
windowSurface = pygame.display.set_mode((size),0,32)
pygame.display.set_caption('Map Test')

#these are the width and height of the game tiles
width = 25
height = 25
screenTileW = 1000 / 25
screenTileH = 800 / 25

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
			pygame.draw.rect(windowSurface,color,(x,y,width,height),0)
			x = x + height + margin
		y=y+width + margin
		x = 0
	drawButtons()

#draws the grid onto the map
def drawGrid():
	x = 25
	y = 25
	z = 625
	a = 25
	b = 25
	c = 975
	glen = len(grid)-7
	#print(glen)
	#for row in range(glen):
	row = 0
	rlen = len(grid[row])-2
	#print(rlen)
	for col in range(rlen):
		#vertical lines
		pygame.draw.lines(windowSurface,white,False,[(x,y),(x,z)],3)
		x=x+25
	for x in range(glen):
		#horizontal lines
		pygame.draw.lines(windowSurface,white,False,[(a,b),(c,b)],3)
		b=b+25


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

def drawButtons():
		drawExample(0)

def drawExample(x):
		#print(x)
		if(x is 0):
			exam = pygame.image.load("ex2.jpg")
			windowSurface.blit(exam,(xlist[1],ylist[27]))
			#pygame.draw.rect(windowSurface,blue,(xlist[1],ylist[27],width*3,height*2),0)
			pygame.display.update()
		else:
			exam = pygame.image.load("ex.jpg")
			windowSurface.blit(exam,(xlist[1],ylist[27]))
			#pygame.draw.rect(windowSurface,red,(xlist[1],ylist[27],width*3,height*2),0)
			pygame.display.update()

def move(coordinate,xy):
	print("COORD", grid[coordinate[1]][coordinate[0]])
	if (grid[coordinate[1]][coordinate[0]] != "7"):
		windowSurface.blit(man,(coordinate[1],coordinate[0]))
		movingX+=1
		print("MOVINGX", movingX)
		pygame.display.flip()
		drawMap(grid)

######################################################################################
#39,31
#reads in the command line argv for the map text file
f = file(sys.argv[1],'r')

# draw the window onto the screen
grid = popGrid(f)
drawMap(grid)
print(exbutton)
pygame.display.update()
xy = 0
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
		if event.type == pygame.MOUSEBUTTONUP:
			mousex, mousey = pygame.mouse.get_pos()
			cord = getGridCord(mousex,mousey)
			print(cord)
			if((exbutton[0] <= xlist[cord[0]] and xlist[cord[0]] < exbutton[2]) and (exbutton[1] <= ylist[cord[1]] and ylist[cord[1]] < exbutton[3])):
				drawExample(1)
			else:
				drawExample(0)

		if event.type == QUIT:
			pygame.quit()
	    		sys.exit()

	####################################################
	#Character movement. Coordinate obtains coordinates#
	#corresponding to Grid[Y][X]. Moves til it finds   #
	#7 in the grid, then readjusts.                    #
	####################################################
	coordinate = getGridCord(movingX,movingY)
	move(coordinate,xy)
