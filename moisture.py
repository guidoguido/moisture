# main
# import threading
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
	prev_time_millitime = int(round(time.time()*1000))
	interval = 1000
	led_on = False
	try:
		while True:
			if error:
				color = "Red"
			elif debug:
				color = "Blue"
			else:
				color = "Green"

			if current_milli_time - prev_time_millitime > interval:
				prev_time_millitime = current_milli_time
				if led_on:
					led.off()
				else:
					led.on(color)
	except (KeyboardInterrupt, SystemExit):
 		GPIO.cleanup()

# def measure(): #function to let all the sensors(1) measure 
# 	interval = 1        
# 	try:
# 		while True:

# 			# Read the sensor data
# 			sensor_level = sensor.ReadChannel()
# 			sensor_volts = sensor.ConvertVolts(sensor_level,2)

# 			# Print out results
# 			print"---"
# 			if not debug:
# 				print("Data: {}".format(sensor_level))
# 			else:
# 				print("Data: {} ({}V)".format(sensor_level,sensor_volts))

# 			# Wait before repeating loop
# 			# time.sleep(interval)
# 	except (KeyboardInterrupt, SystemExit):
# 		GPIO.cleanup()

status_indicator()