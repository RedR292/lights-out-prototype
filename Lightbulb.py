from timerThread import LightbulbTimer
import pygame
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
