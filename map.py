import pygame
from pygame.locals import *
import sys

screen_width = 800
screen_height = 800

width = 12
height = 12
margin = 1

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
color = red
windowSurface = pygame.display.set_mode((screen_width,screen_height),0,32)

pygame.display.set_caption('Map Test')
x = 0
y = 0 

f = file(sys.argv[1],'r')


grid = []
row = 0
for xy in (f):
	grid.append([])
	for dxdy in xy:
		grid[row].append(dxdy)
	row = row+1


index = 0
for row in grid:
	row.pop() #End everyline, including last line of map with /n
	for column in row:
		print(column)
		if(column == "0"):
			color = green
		if(column == "1"):
			color = red
		if(column == "2"):
			color = blue
		pygame.draw.rect(windowSurface,color,(x,y,width,height),0)
		x = x + height + margin
	y=y+width+margin
	x = 0	
	#pygame.draw.rect(windowSurface,red,(x,y,width,height),0)



# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
		print(grid)
            	pygame.quit()
            	sys.exit()

