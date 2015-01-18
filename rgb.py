#class to controll rgb led 
import RPi.GPIO as GPIO, time, os

GPIO.setmode(GPIO.BCM)

class RGB(object):
	def __init__(self,red,green,blue,debug):
		self.red = red
		self.green = green
		self.blue = blue
		self.debug = debug

		GPIO.setup(red, GPIO.OUT)
		GPIO.setup(green, GPIO.OUT)
		GPIO.setup(blue, GPIO.OUT)
	
	def blink(self, color, blink_time, pause_time):
		try:
			while True:
				if color == "Blue":
					GPIO.output(red, False)
					GPIO.output(green, False)
					GPIO.output(blue, True)
					
					## sleep
					time.sleep(pause_time)

					GPIO.output(red, False)
					GPIO.output(green, False)
					GPIO.output(blue, False)

					## sleep
					time.sleep(pause_time)

