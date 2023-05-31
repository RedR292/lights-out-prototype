'''DEFINITION:
This ptype works to implement the <Timer> and more general <Threading>
modules in order to implement event synching'''
import pygame
from timerThread import LightbulbTimer
from pynput.mouse import Listener
class Lightbulb(pygame.sprite.Sprite):
	def __init__(self):
		super(Lightbulb,self).__init__()
		self.surf=pygame.Surface((70,70))
		self.surf.fill(('#FFFFFF'))
		self.broken=False
		self.unscrewTimer=None; self.rescrewTimer=None
		self.unscrewSeconds=10; self.rescrewSeconds=0
	#END init

	##Starts or cancels the appropriate timer and updates timings
	def manageTimers(self, isUnscrew: bool, isStarted=True):
		if isUnscrew:
			if isStarted:
				self.unscrewTimer=LightbulbTimer(self.unscrewSeconds,self.breakBulb)
				self.unscrewTimer.start()
			else:
				self.rescrewSeconds=10-int(self.unscrewTimer.remaining())
				self.unscrewTimer.cancel()
			#ENDELSE
		#ENDIF
		else:
			if isStarted:
				self.rescrewTimer=LightbulbTimer(self.rescrewSeconds,self.rescrew)
				self.rescrewTimer.start()
			else:
				self.unscrewSeconds=10-int(self.rescrewTimer.remaining())
				self.rescrewTimer.cancel()
			#ENDELSE
		#ENDIF
	#END manageTimers

	def isBroken(self):
		return self.broken
	#END isBroken

	def rescrew(self):
		print("lightbulb fully screwed in")
	#END rescrew

	def breakBulb(self):
		self.broken=True

	##Unscrews the lightbulb
	def unscrew(self):
		print('Lightbulb began unscrewing')
		unscrewTimeSeconds=10.0
		self.manageTimers(True) #start unscrewTimer
	#END unscrew
#ENDCLASS

#test usage
lb=Lightbulb()
lb.unscrew()
def on_click(x,y,button,pressed):
	if pressed and lb.unscrewTimer.is_alive():
		lb.manageTimers(True,False) #stop unscrewtimer
		print(f"Lightbulb need be rescrewed for another {lb.rescrewSeconds} seconds")
		lb.manageTimers(False) #start rescrew timer
	#ENDIF
	if not pressed and lb.rescrewTimer.is_alive():
		lb.manageTimers(False,False) #stop rescrew timer
		print(f'Lightbulb is {lb.unscrewSeconds} seconds away from breaking')
	#ENDIF
#END on_click

clickListener=Listener(on_click=on_click)
clickListener.start()

while True:
	if lb.isBroken():
		print("Lightbulb broke")
		break
