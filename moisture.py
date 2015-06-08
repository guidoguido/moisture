# main
# import threading
import RPi.GPIO as GPIO
import time
from mst_sensor import Sensor
from rgb import RGB 

current_milli_time = lambda: int(round(time.time() * 1000))
debug = True
error = False

sensor = Sensor(0, debug)
led = RGB(23,24,25)

#fucntion to show in which mode is running or if there is a problem
def status_indicator():
	prev_milli_time = int(round(time.time()*1000))
	interval = 0
	led_on = False
	try:
		while True:
			if error:
				color = "Red"
			elif debug:
				color = "Blue"
			else:
				color = "Green"

			if current_milli_time() - prev_milli_time > interval:	#Timer 
				prev_milli_time = int(current_milli_time())					#prev time is updated
				if led_on:
					interval = 4000	#interval between blinks
					led.off()
					led_on = False
				else:
					interval = 100	#blink durration
					led.on(color)
					led_on = True
	except (KeyboardInterrupt, SystemExit):
 		GPIO.cleanup()

def measure(): #function to let all the sensors(1) measure 
  prev_milli_time = int(round(time.time()*1000))
  interval = 3
try:
		while True:
			if current_milli_time() - prev_milli_time > interval:	#Timer 
				prev_milli_time = int(current_milli_time())

				# Read the sensor data
				sensor_level = sensor.ReadChannel()
				sensor_volts = sensor.ConvertVolts(sensor_level,2)

				# Print out results
				print"---"
				if not debug:
					print("Data: {}".format(sensor_level))
				else:
					print("Data: {} ({}V)".format(sensor_level,sensor_volts))
	except (KeyboardInterrupt, SystemExit):
		GPIO.cleanup()

status_indicator()
measure()