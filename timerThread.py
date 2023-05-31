from threading import Timer
from time import time

class LightbulbTimer(Timer):
	startTime=None
	def start(self):
		self.startTime=time()
		Timer.start(self)
	#END start
	def elapsed(self):
		elapsed=time()-self.startTime
		return elapsed
	#END elapsedTime
	def remaining(self):
		timeRemaining=int(self.interval-self.elapsed())
		return timeRemaining
