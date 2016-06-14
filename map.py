from __future__ import print_function
import pygame
from pygame.locals import *
import sys



red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
gray = (100,100,100)
color = red


pygame.init()

size = (1000,800)
width = 25
height = 25

windowSurface = pygame.display.set_mode((size),0,32)


pygame.display.set_caption('Map Test')


x = 0
y = 0 
margin = 0
f = file(sys.argv[1],'r')


grid = []
row = 0
for xy in (f):
	grid.append([])
	for dxdy in xy:
		grid[row].append(dxdy)
	row = row+1

xnum = len(grid)-1
ynum = len(grid[0])-1




for row in grid:
	row.pop() #End everyline, including last line of map with /n
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

	
def drawGrid():
	x = 25
	y = 25
	z = 625
	a = 25
	b = 25
	c = 975
	for row in grid:
		for col in row:
			pygame.draw.lines(windowSurface,white,False,[(a,b),(c,b)],3)
			pygame.draw.lines(windowSurface,white,False,[(x,y),(x,z)],3)
			x=x+25
		b=b+25
		
		

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
	gswitch = pygame.key.get_pressed()[K_g]
	if(gswitch == 1):
		drawGrid()
		pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	    		sys.exit()
	

