from __future__ import print_function
import pygame
from pygame.locals import *
import sys


#const color with the RGB values
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
gray = (100,100,100)



pygame.init()

#size is width x heigth of the window that opens
size = (1000,800)
windowSurface = pygame.display.set_mode((size),0,32)
pygame.display.set_caption('Map Test')

#these are the width and height of the game tiles
width = 25
height = 25

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
		
#reads in the command line argv for the map text file
f = file(sys.argv[1],'r')

# draw the window onto the screen
grid = popGrid(f)
drawMap(grid)
pygame.display.update()

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
		if event.type == QUIT:
			pygame.quit()
	    		sys.exit()
	

