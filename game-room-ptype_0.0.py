##tkinter prototype for the game room of lights out
import tkinter as tk
from math import ceil

##get window dimensions and offsets wrt. the screen
def buildWindow():
	width=1920
	height=1080
	# print(height) #debug statement
	xOffset=yOffset=0
	geometryString=f'{width}x{height}+{xOffset}+{yOffset}'
	# print(geometryString) #debug statement
	window=tk.Tk()
	window.geometry(geometryString)
	return (window,width,height)
#END buildWindow

##Build and place the frames
def buildFrames(window: tuple):
	# names=['gameFrame','bulbFrame','deadFrame','scaryFrame']
	# colours=['#000000','#FDDC5C','#FF0000','#A020F0']
	_,width,height=window
	gameWidth=int(width*0.47); scaryWidth=int(width*0.53)
	bulbHeight=int(height*0.52)
	# print(gameWidth) #debug statement
	gameFrame=tk.Frame(width=gameWidth, bg='#000000')
	scaryFrame=tk.Frame(width=scaryWidth, bg='#A020F0')
	bulbFrame=tk.Frame(master=gameFrame, height=bulbHeight, bg='#FDDC5C')
	deadFrame=tk.Frame(master=gameFrame, width=gameWidth, bg='#FF0000')
	bulbFrame.pack_propagate(False) #prevents frame shrinking to fit widgets
	gameFrame.pack(side=tk.LEFT, fill=tk.BOTH)
	scaryFrame.pack(side=tk.LEFT, fill=tk.BOTH)
	bulbFrame.pack(side=tk.TOP, fill=tk.BOTH)
	deadFrame.pack(side=tk.TOP, fill=tk.BOTH)
	return gameFrame, scaryFrame, bulbFrame, deadFrame
	# print(f'expected scary width: {scaryWidth}\nActual width: {scaryFrame.winfo_width()}') #debug statement
#END buildFrames

##Build and place the buttons to represent the lightbulbs
def buildButtons(frame):
	buttons=[[tk.Button()]*3]*3
	buttonX=210; buttonY=70; buttonCount=0
	#Build the buttons
	for buttonRows in buttons:
		for button in buttonRows:
			button=tk.Button(master=frame,width=10,height=4,text=f'Button {buttonCount}')
			button.place(x=buttonX,y=buttonY)
			buttonX+=170; buttonCount+=1
		#ENDFOR
		buttonX=210; buttonY+=170
	#ENDFOR
	return buttons
#END buildButtons

windowTuple=window,windowWidth,windowHeight=buildWindow()
gameFrame,scaryFrame,bulbFrame,deadFrame=buildFrames(windowTuple)
buttons=buildButtons(bulbFrame)
window.mainloop() #LAST LINE!
