#class to controll rgb led 
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

class RGB(object):
	def __init__(self,red,green,blue,debug):
		self.red = red
		self.green = green
		self.blue = blue
		self.debug = debug

		GPIO.setup(self.red, GPIO.OUT)
		GPIO.setup(self.green, GPIO.OUT)
		GPIO.setup(self.blue, GPIO.OUT)
	
	def blink(self, color, blink_time, pause_time):
		while True:
			PIO.output(self.blue, True)
			print "On"
			time.sleep(blink_time)
			GPIO.output(self.blue, False)
			time.sleep(pause_time)
			print "Off"
		'''if color == "Blue":
			while True:
				PIO.output(self.blue, True)
				time.sleep(blink_time)
				GPIO.output(self.blue, False)
				time.sleep(pause_time)

		elif color == "Green":
			GPIO.output(self.green, True)
			
		# delay still freezes complete system for total pause time
			time.sleep(pause_time)

			GPIO.output(self.green, False)
		'''
		return None