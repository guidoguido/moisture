#class to controll rgb led 
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

class RGB(object):
	def __init__(self,red,green,blue):
		self.red = red
		self.green = green
		self.blue = blue
		self.state = False

		GPIO.setup(self.red, GPIO.OUT)
		GPIO.setup(self.green, GPIO.OUT)
		GPIO.setup(self.blue, GPIO.OUT)
		GPIO.output(self.red, False)
		GPIO.output(self.green, False)
		GPIO.output(self.blue, False)
	
	def on(self, color):
		if color == "Red":
			GPIO.output(self.red, True)
		elif color == "Green":
			GPIO.output(self.green, True)
		elif color == "Blue":
			GPIO.output(self.blue, True)
		self.state = True

	def off(self):
		GPIO.output(self.red, False)
		GPIO.output(self.green, False)
		GPIO.output(self.blue, False)
		self.state = False

	def getState():
		return self.state

	def setState(state):
		self.state = state