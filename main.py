from __future__ import print_function
import pygame
from pygame.locals import *
import sys
from tower import Tower
from map import Map
from minion import Minions
import constants

def main(arg):
	f = file(arg,'r')
	clock = pygame.time.Clock()
	bullets = []

	level = Map(f)

	level.popGrid(f)
	level.drawMap()

	exswitch = False
	exswitch2 = False
	towerArray = []
	minions = []
	t_minions = 1


	# run the game loop
	while True:
		gswitch = pygame.key.get_pressed()[K_g]
		cswitch = pygame.key.get_pressed()[K_c]
		pswitch = pygame.key.get_pressed()[K_p]
		if(pswitch == 1):
			print ("Score :", level.score)
			level.bool = True
			while level.bool is True:
				if(t_minions <= 10):
					minions.append(Minions(level))
					level.moveX(minions)
					t_minions = t_minions + 1
				else:
					mousex, mousey = pygame.mouse.get_pos()
					#print("MOUSE",mousex,mousey)
					level.moveX(minions)
				level.live_out()
				level.score_out()
				#level.money_out()
				#level.blit_update()
				if(not minions):
					level.bool = False
					level.level = level.level + 1
					t_minions = 1
					print("success")
				for x in range(len(minions)):
					print(minions[x].HP)
				print('\n')
				for x in minions:
					for y in towerArray:
						if(y.pingTower(x) is True):
							level.bulletShoot(x,y)
							if(y.damMini(x) is True):
								level.score = level.score + x.score
								level.score_out()
								minions.remove(x)
							break
					break
				level.blit_update()


		if(gswitch == 1):
			level.drawGrid()
			level.drawRange(towerArray)
		if(cswitch == 1):
			thing = True
			level.drawMap()

		for event in pygame.event.get():
			if(exswitch is True and event.type is pygame.MOUSEBUTTONDOWN):
				mousex, mousey = pygame.mouse.get_pos()
				cord = level.getGridCord(mousex,mousey)
				temporary = Tower(1)
				if (level.canPutTower(cord[0],cord[1]) is True):
					if(level.money - temporary.cost) >= 0 :
						level.windowSurface.blit(constants.REDTOWER,(level.xlist[cord[0]],level.xlist[cord[1]]))
						level.grid[cord[1]][cord[0]] = '5'
						mytower = Tower(1,level.xlist[cord[1]],level.xlist[cord[0]])
						towerArray.append(mytower)
						level.money = level.money - mytower.cost
						#level.money_out()
						print("MONEYS",level.money)
					else:
						print("Insufficient funds")
				exswitch = False
				level.drawMap()

		if(exswitch2 is True and event.type is pygame.MOUSEBUTTONDOWN):
			mousex, mousey = pygame.mouse.get_pos()
			cord = level.getGridCord(mousex,mousey)
			if (level.canPutTower(cord[0],cord[1]) is True and level.canPutTower(cord[0],cord[1]+1) is True and level.canPutTower(cord[0]+1,cord[1]+1) is True and level.canPutTower(cord[0]+1,cord[1]) is True):
				pygame.draw.rect(level.windowSurface,constants.BLACK,(level.xlist[cord[0]],level.xlist[cord[1]],level.width,level.height),0)
				pygame.draw.rect(level.windowSurface,constants.BLACK,(level.xlist[cord[0]],level.xlist[cord[1]+1],level.width,level.height),0)
				pygame.draw.rect(level.windowSurface,constants.BLACK,(level.xlist[cord[0]+1],level.xlist[cord[1]+1],level.width,level.height),0)
				pygame.draw.rect(level.windowSurface,constants.BLACK,(level.xlist[cord[0]+1],level.xlist[cord[1]],level.width,level.height),0)
				level.grid[cord[1]][cord[0]] = '6'
				level.grid[cord[1]][cord[0]+1] = '6'
				level.grid[cord[1]+1][cord[0]+1] = '6'
				level.grid[cord[1]+1][cord[0]] = '6'
				mytower = Tower(2,level.xlist[cord[1]],level.xlist[cord[0]])
				towerArray.append(mytower)
			exswitch2 = False
			level.drawMap()

		if event.type == pygame.MOUSEBUTTONDOWN:
			mousex, mousey = pygame.mouse.get_pos()
			cord = level.getGridCord(mousex,mousey)
			if((level.exbutton[0] <= level.xlist[cord[0]] and level.xlist[cord[0]] < level.exbutton[2]) and (level.exbutton[1] <= level.ylist[cord[1]] and level.ylist[cord[1]] < level.exbutton[3])):
				level.drawGrid()
				level.drawRange(towerArray)
				level.drawRedButton(1)
				exswitch = True

			elif((level.exbutton2[0] <= level.xlist[cord[0]] and level.xlist[cord[0]] < level.exbutton2[2]) and (level.exbutton2[1] <= level.ylist[cord[1]] and level.ylist[cord[1]] < level.exbutton2[3])):
				level.drawGrid()
				level.drawRange(towerArray)
				level.drawBlueButton(1)
				exswitch2 = True
			else:
				level.drawRedButton(0)
				exswitch2 = False
				level.drawBlueButton(0)
				exswitch = False



		if event.type == QUIT:
			pygame.quit()
		    	sys.exit()

if __name__ == '__main__':
	arg = sys.argv[1]
	main(arg)
