'''LightbulbManager handles the use of a 3 by 3 grid of lightbulbs and
handles user input to control their states'''
import pygame
from Lightbulb import Lightbulb
from random import randint as rand
class LightbulbManager():
	def __init__(self):
		super(LightbulbManager,self).__init__()
		self.focusedBulb=None
		self.lightbulbs=[]
		x=220; y=70
		for i in range(3):
			row=[]
			for j in range(3):
				row.append(Lightbulb(x,y))
				x+=170
			#ENDFOR
			self.lightbulbs.append(row)
			x=220; y+=170
		#ENDFOR
		# print(self.lightbulbs) #debug statement
	#END init

	##Start unscrewing a lightbulb at random
	##Repeats randomisation if lb is already unscrewing
	def unscrew(self):
		noSelected=True
		while noSelected:
			random_i=rand(0,2); random_j=rand(0,2)
			lb=lbs[random_i][random_j]
			if not lb.isUnscrewing():
				noSelected=True
		#ENDWHILE -> lb is chosen
		lb.unscrew()
	#END unscrew

	##Start rescrewing a chosen lightbulb
	def rescrew(self):
		self.focusedBulb.rescrew()
	#END rescrew

	def stopRescrewing(self):
		self.focusedBulb.stopRescrewing()
		self.focusedBulb=None

	def getDisplay(self,x,y):
		lb=self.lightbulbs[x][y]
		return lb.getDisplay()

	def checkForClick(self,coords):
		for row in range(3):
			for col in range(3):
				lb=self.lightbulbs[row][col]
				if lb.isClicked(coords):
					print("Lightbulb was clicked!")
					self.focusedBulb=lb

#ENDCLASS

def testClass():
	lbm=LightbulbManager()

# testClass()
