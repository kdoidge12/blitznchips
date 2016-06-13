import pygame
from pygame.locals import *

screen_width = 600
screen_height = 600

width = 45
height = 45
margin = 2

red = (255,0,0)
green = (0,255,0)
color = red
windowSurface = pygame.display.set_mode((screen_width,screen_height),0,32)

pygame.display.set_caption('Map Test')
x = 0
y = 0 

grid = []

for row in range(13):
	grid.append([])
	for col in range(3):
		if(col is 1):
			grid[row].append(2)
		else:
			grid[row].append(0)
index = 0
for row in range(13):	
	for col in range(3):
		if(col is 1):
			color = green
		else:
			color = red
		pygame.draw.rect(windowSurface,color,(x,y,width,height),0)
		y = y + height + margin
	x = x + width + margin
	y = 0
	
	
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



