##Test to make sure the pygame environment works for the visual ptype
from LightbulbManager import LightbulbManager
import pygame
from threading import Timer
pygame.init()

# TODO: REDESIGN TIMERS SUCH THAT THEY ARE NOT NONE WHEN INIT'D

##Build and colour the surfs
def buildSurfs():
	vars=globals() #global variable dict
	names=['game','scary','bulb','dead']
	sizes=[(902,1080),(1018,1080),(902,561),(902,518)]
	colours=['#FFFFFF','#A020F0','#FDDC5C','#FF0000']
	for surf in range(4):
		name=f'{names[surf]}Surf'
		vars[name]=pygame.Surface(sizes[surf])
		vars[name].fill(colours[surf])
	#ENDFOR
#END buildSurfs -> surfs are now vars

##Display the bulbs from lbm onto surface
def displayBulbs(surface,lbm):
	for bulb_x in range(3):
		for bulb_y in range(3):
			displayData=lbm.getDisplay(bulb_x,bulb_y)
			surface.blit(*displayData)
	#ENDFOR
#END displayBulbs

##Display the surfs to the room
def displaySurfaces():
	screen.blit(gameSurf,(0,0))
	screen.blit(scarySurf,(903,0))
	gameSurf.blit(bulbSurf,(0,0))
	gameSurf.blit(deadSurf,(0,562))
#END displaySurfaces

##Display the room to the screen
def displayRoom():
	screen.fill('#000000')
	displaySurfaces() #This line comes first
	displayBulbs(bulbSurf,lbm)
#END displayRoom

##Sets up the functional game constructs
def setupGame():
	vars=globals()
	vars['screen']=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
	vars['tick']=pygame.display.flip
	vars['lbm']=LightbulbManager()
	buildSurfs()
#END setupGame

def unscrew():
	Timer(10,unscrew).start()
	# print("tried to unscrew a bulb")
	lbm.unscrew()

##MAIN GAME LOOP
def gameLoop():
	running=True
	unscrew()
	while running:
		displayRoom()
		for event in pygame.event.get():
			type=event.type
			if type==pygame.QUIT:
				running=False
			elif type==pygame.MOUSEBUTTONDOWN:
				pos=pygame.mouse.get_pos()
				lbm.checkForClick(pos)
			elif type==pygame.MOUSEBUTTONUP:
				lbm.stopRescrewing()
		tick()

setupGame()
gameLoop()
