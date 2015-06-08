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

def blink_status(): #fucntion to show in which mode is running or if there is a problem
	
	if error:
		color = "Red"
	elif debug:
		color = "Blue"
	else:
		color = "Green"
	if led.getState():
		# interval = 4000	#interval between blinks
		led.off()
	else:
		# interval = 100	#blink durration
		led.on(color)

def measure(): #function to let all the sensors(1) measure 
	# Read the sensor data
	sensor_level = sensor.ReadChannel()
	sensor_volts = sensor.ConvertVolts(sensor_level,2)

	# Print out results
	print"---"
	if not debug:
		print("Data: {}".format(sensor_level))
	else:
		print("Data: {} ({}V)".format(sensor_level,sensor_volts))

def timer(): #function to time multiple events
	prev_milli_time_1 = int(round(time.time()*1000))
	prev_milli_time_2 = int(round(time.time()*1000))
	blink_interval = 100
	measure_interval = 5000
	try:
		while True:
			if current_milli_time() - prev_milli_time_1 > blink_interval:	#Timer 
				prev_milli_time_1 = int(current_milli_time())
				blink_status()

				if led.getState() 
					blink_interval = 100
				else
					blink_interval = 2900

			if current_milli_time() - prev_milli_time_2 > measure_interval:	#Timer 
				prev_milli_time_2 = int(current_milli_time())
				measure()

	except Exception, e:
		raise
	else:
		pass
	finally:
		GPIO.cleanup()

timer()