from __future__ import print_function
import pygame
from pygame.locals import *
import sys
import map
import tower
import consats

f = file('grid.txt','r')

grid = map.popGrid(f)
map.drawMap(grid)
pygame.display.update()

exswitch = False
exswitch2 = False

# run the game loop
while True:
	gswitch = pygame.key.get_pressed()[K_g]
	cswitch = pygame.key.get_pressed()[K_c]
	if(gswitch == 1):
		map.drawGrid(grid)
	if(cswitch == 1):
		map.drawMap(grid)

	for event in pygame.event.get():
		if(exswitch is True and event.type is pygame.MOUSEBUTTONDOWN):
			mousex, mousey = pygame.mouse.get_pos()
			cord = map.getGridCord(mousex,mousey)
			if (tower.canPutTower(cord[0],cord[1],grid) is True):
				map.windowSurface.blit(consats.REDTOWER,(map.xlist[cord[0]],map.xlist[cord[1]]))
				grid[cord[1]][cord[0]] = '5'
			exswitch = False
			map.drawMap(grid)

	if(exswitch2 is True and event.type is pygame.MOUSEBUTTONDOWN):
		mousex, mousey = pygame.mouse.get_pos()
		cord = map.getGridCord(mousex,mousey)
		if (tower.canPutTower(cord[0],cord[1],grid) is True and tower.canPutTower(cord[0],cord[1]+1,grid) is True and tower.canPutTower(cord[0]+1,cord[1]+1,grid) is True and tower.canPutTower(cord[0]+1,cord[1],grid) is True):
			pygame.draw.rect(map.windowSurface,consats.BLACK,(map.xlist[cord[0]],map.xlist[cord[1]],map.width,map.height),0)
			pygame.draw.rect(map.windowSurface,consats.BLACK,(map.xlist[cord[0]],map.xlist[cord[1]+1],map.width,map.height),0)
			pygame.draw.rect(map.windowSurface,consats.BLACK,(map.xlist[cord[0]+1],map.xlist[cord[1]+1],map.width,map.height),0)
			pygame.draw.rect(map.windowSurface,consats.BLACK,(map.xlist[cord[0]+1],map.xlist[cord[1]],map.width,map.height),0)
			grid[cord[1]][cord[0]] = '6'
			grid[cord[1]][cord[0]+1] = '6'
			grid[cord[1]+1][cord[0]+1] = '6'
			grid[cord[1]+1][cord[0]] = '6'
		exswitch2 = False
		map.drawMap(grid)

	if event.type == pygame.MOUSEBUTTONDOWN:
		mousex, mousey = pygame.mouse.get_pos()
		cord = map.getGridCord(mousex,mousey)
		if((map.exbutton[0] <= map.xlist[cord[0]] and map.xlist[cord[0]] < map.exbutton[2]) and (map.exbutton[1] <= map.ylist[cord[1]] and map.ylist[cord[1]] < map.exbutton[3])):
			map.drawGrid(grid)
			tower.drawRedButton(1)
			exswitch = True

		elif((map.exbutton2[0] <= map.xlist[cord[0]] and map.xlist[cord[0]] < map.exbutton2[2]) and (map.exbutton2[1] <= map.ylist[cord[1]] and map.ylist[cord[1]] < map.exbutton2[3])):
			map.drawGrid(grid)
			tower.drawBlueButton(1)
			exswitch2 = True
		else:
			tower.drawRedButton(0)
			exswitch2 = False
			tower.drawBlueButton(0)
			exswitch = False

	if event.type == QUIT:
		pygame.quit()
	    	sys.exit()