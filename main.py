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

	#init Map(grid, money, score, lives) depending on level
	level = Map(f, 200, 0, 20)

	level.popGrid(f)
	level.drawMap()

	exswitch = False
	exswitch2 = False
	startswitch = False
	helpswitch = False
	returnswitch = False
	towerArray = []
	minions = []
	t_minions = 1


	# run the game loop
	while True:
		gswitch = pygame.key.get_pressed()[K_g]
		cswitch = pygame.key.get_pressed()[K_c]
		pswitch = pygame.key.get_pressed()[K_p]
		while level.bool is True:
			if(t_minions <= 10):
				minions.append(Minions(level))
				level.moveX(minions)
				t_minions = t_minions + 1
			else:
				mousex, mousey = pygame.mouse.get_pos()
				#print("MOUSE",mousex,mousey)
				level.moveX(minions)
			#level.live_out()
			#level.score_out()
			level.updateLevel()
			level.updateLives()
			level.updateScore()
			level.updateMoney()
				#level.money_out()
				#level.blit_update()
			if(not minions):
				level.bool = False
				level.level = level.level + 1
				level.moveX([])
				level.updateLevel()
				level.updateLives()
				level.updateScore()
				level.updateMoney()
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
							level.updateScore()
							#level.score_out()
							level.money = level.money + x.value
							#level.updateMoney()
							try:
								minions.remove(x)
							except ValueError:
								pass
							print("LEVELmoney", level.money)
						#break
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
						level.updateMoney()
						print("MONEYS",level.money)
					else:
						print("Insufficient funds")
				exswitch = False
				level.drawMap()

		if(exswitch2 is True and event.type is pygame.MOUSEBUTTONDOWN):
			mousex, mousey = pygame.mouse.get_pos()
			cord = level.getGridCord(mousex,mousey)
			temporary = Tower(2)
			if (level.canPutTower(cord[0],cord[1]) is True and level.canPutTower(cord[0],cord[1]+1) is True and level.canPutTower(cord[0]+1,cord[1]+1) is True and level.canPutTower(cord[0]+1,cord[1]) is True):
				if((level.money - temporary.cost) >= 0):
					pygame.draw.rect(level.windowSurface,constants.BLACK,(level.xlist[cord[0]],level.xlist[cord[1]],level.width*2,level.height*2),0)
					pygame.draw.rect(level.windowSurface,constants.BLACK,(level.xlist[cord[0]],level.xlist[cord[1]+1],level.width,level.height),0)
					pygame.draw.rect(level.windowSurface,constants.BLACK,(level.xlist[cord[0]+1],level.xlist[cord[1]+1],level.width,level.height),0)
					pygame.draw.rect(level.windowSurface,constants.BLACK,(level.xlist[cord[0]+1],level.xlist[cord[1]],level.width,level.height),0)
					level.grid[cord[1]][cord[0]] = '6'
					level.grid[cord[1]][cord[0]+1] = 'A'
					level.grid[cord[1]+1][cord[0]+1] = 'A'
					level.grid[cord[1]+1][cord[0]] = 'A'
					mytower = Tower(2,level.xlist[cord[1]],level.xlist[cord[0]])
					towerArray.append(mytower)
					level.money = level.money - mytower.cost
					level.updateMoney()
					print("MONEYS",level.money)
				else:
					print("Insufficient funds")
			exswitch2 = False
			level.drawMap()

		if event.type == pygame.MOUSEBUTTONDOWN:
			mousex, mousey = pygame.mouse.get_pos()
			cord = level.getGridCord(mousex,mousey)
			if((level.exbutton[0] <= level.xlist[cord[0]] and level.xlist[cord[0]] < level.exbutton[2]) and (level.exbutton[1] <= level.ylist[cord[1]] and level.ylist[cord[1]] < level.exbutton[3])):
				level.drawGrid()
				level.drawTowerInfo(1)
				level.drawRange(towerArray)
				level.drawRedButton(1)
				exswitch = True

			elif((level.exbutton2[0] <= level.xlist[cord[0]] and level.xlist[cord[0]] < level.exbutton2[2]) and (level.exbutton2[1] <= level.ylist[cord[1]] and level.ylist[cord[1]] < level.exbutton2[3])):
				level.drawGrid()
				level.drawTowerInfo(2)
				level.drawRange(towerArray)
				level.drawBlueButton(1)
				exswitch2 = True

			elif((level.startbutton[0] <= level.xlist[cord[0]] and level.xlist[cord[0]] < level.startbutton[2]) and (level.startbutton[1] <= level.ylist[cord[1]] and level.ylist[cord[1]] < level.startbutton[3])):
				#level.popupWindow('Wave Starting')
				level.drawStartButton(1)
				level.bool = True
				startswitch = True

			elif((level.helpbutton[0] <= level.xlist[cord[0]] and level.xlist[cord[0]] < level.helpbutton[2]) and (level.helpbutton[1] <= level.ylist[cord[1]] and level.ylist[cord[1]] < level.helpbutton[3])):
				level.popupWindow('Controls key g: display grid ')
				level.drawHelpButton(1)
				helpswitch = True

			elif((level.returnbutton[0] <= level.xlist[cord[0]] and level.xlist[cord[0]] < level.returnbutton[2]) and (level.returnbutton[1] <= level.ylist[cord[1]] and level.ylist[cord[1]] < level.returnbutton[3])):
				level.drawReturnButton(1)
				pygame.quit()
				sys.exit()
				returnswitch = True
			else:
				level.drawRedButton(0)
				exswitch2 = False
				level.drawBlueButton(0)
				exswitch = False
				level.drawStartButton(0)
				level.drawReturnButton(0)
				level.drawHelpButton(0)
				startswitch = False
				helpswitch = False
				returnswitch = False



		if event.type == QUIT:
			pygame.quit()
		    	sys.exit()

if __name__ == '__main__':
	arg = sys.argv[1]
	main(arg)
