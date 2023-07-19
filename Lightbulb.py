from timerThread import LightbulbTimer
import pygame
class Lightbulb(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Lightbulb,self).__init__()
		self.surf=pygame.Surface((70,70))
		self.rect=pygame.Rect(x,y,70,70)
		self.surf.fill(('#FFFFFF'))
		self.broken=False
		self.unscrewTimer=None; self.rescrewTimer=None
		self.unscrewSeconds=10; self.rescrewSeconds=0
		self.x=x; self.y=y
		self.state=0
	#END init

	##Starts or cancels the appropriate timer and updates timings
	def manageTimers(self, isUnscrew: bool, isStarted=True):
		if isUnscrew:
			timer=self.unscrewTimer; otherTimer=self.rescrewTimer
			timeSeconds=self.unscrewSeconds
			otherTimeSeconds=self.rescrewSeconds
			timer_function=self.breakBulb
		#ENDIF
		else:
			timer=self.rescrewTimer; otherTimer=self.unscrewTimer
			timeSeconds=self.rescrewSeconds
			otherTimeSeconds=self.unscrewSeconds
			timer_function=self.rescrew
		#ENDELSE
		if isStarted:
			timer=LightbulbTimer(timeSeconds,timer_function)
			timer.start()
		#ENDIF
		else:
			timeSeconds=int(timer.remaining()) #might be redundent line
			otherTimeSeconds=10-int(timer.remaining())
			timer.cancel()
		#ENDELSE
	#END manageTimers

	def isBroken(self):
		return self.broken
	#END isBroken

	def breakBulb(self):
		self.broken=True
		self.state=-1
	#END breakBulb

	def isUnscrewing(self):
		return self.unscrewTimer.is_alive()
	#END isUnscrewing

	def isRescrewing(self):
		return self.rescrewTimer.is_alive()
	#END isRescrewing

	##Unscrews the lightbulb
	def unscrew(self):
		# print('Lightbulb began unscrewing') #debug statement
		self.unscrewTimeSeconds=10.0
		self.manageTimers(True) #start unscrewTimer
		self.state=1
	#END unscrew

	##Rescrews a lightbulb
	def rescrew(self):
		self.manageTimers(True, False) #stop unscrew timer
		self.manageTimers(False) #start rescrew timer
		self.state=2
	#END rescrew

	def stopRescrewing(self):
		self.manageTimers(False, False)

	##Gets a bulb and it's coords for displaying
	##x,y must be in the range (0,3]
	def getDisplay(self):
		return (self.surf,(self.x,self.y))

	def isClicked(self,coords):
		collided=self.rect.collidepoint(coords)
		return collided
	#isClicked

#ENDCLASS

def testClass():
	pass
	# TODO: BUILD TEST FOR TIMERS AND STATES
