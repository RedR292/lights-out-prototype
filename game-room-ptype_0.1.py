##Test to make sure the pygame environment works for the visual ptype
from Lightbulb import Lightbulb
import pygame
pygame.init()

screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
tickGameClock=pygame.display.flip
##game, scary, and subordinate surfaces
gameSurf=pygame.Surface((902,1080))
scarySurf=pygame.Surface((1018,1080))
bulbSurf=pygame.Surface((902,561))
deadSurf=pygame.Surface((902,518))
gameSurf.fill('#FFFFFF')
scarySurf.fill('#A020F0')
bulbSurf.fill('#FDDC5C')
deadSurf.fill('#FF0000')

lightbulbs=[]
for bulbRows in range(3):
	bulbRow=[]
	for lightbulb in range(3):
		bulbRow.append(Lightbulb())
	lightbulbs.append(bulbRow)

def displayBulbs(surface):
	offsetX=220; offsetY=70
	for bulbRows in lightbulbs:
		for lightbulb in bulbRows:
			surface.blit(lightbulb.surf,(offsetX,offsetY))
			lightbulb.rect=pygame.Rect(offsetX,offsetY,70,70)
			# print(lightbulb.rect)
			offsetX+=170
		#ENDFOR
		offsetX=220; offsetY+=170
	#ENDFOR
#END displayBulbs

def displaySurfaces():
	screen.blit(gameSurf,(0,0))
	screen.blit(scarySurf,(903,0))
	gameSurf.blit(bulbSurf,(0,0))
	gameSurf.blit(deadSurf,(0,562))
#END displaySurfaces

running=True
while running:
	screen.fill('#000000')
	displaySurfaces()
	displayBulbs(bulbSurf)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type==pygame.MOUSEBUTTONDOWN:
			pos=pygame.mouse.get_pos()
			for bulbRow in lightbulbs:
				for lightbulb in bulbRow:
					if lightbulb.rect.collidepoint(pos):
						print("Clicked on a lb")
						break
	tickGameClock()
