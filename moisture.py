# main
# import threading
import RPi.GPIO as GPIO
import time
from datetime import datetime
from mst_sensor import Sensor
from rgb import RGB 

current_milli_time = lambda: int(round(time.time() * 1000))
debug = True
error = False

#sensor = Sensor(0, debug)
led = RGB(23,24,25)

sensors = []
sensors.append(Sensor(01,moist,0,debug))
sensors.append(Sensor(02,moist,1,debug))

def blink_status(): #function to show in which mode is running or if there is a problem
	
	if error:
		color = "Red"
	elif debug:
		color = "Blue"
	else:
		color = "Green"

	if led.getState(): #check the current state of RGB led
		led.off()
	else:
		led.on(color)

def measure(): #function to let all the sensors(2) measure 
	
	#loop through all connected sensors
	for sensor in sensors:
		#get data from sensor
		sensor_level = sensor.ReadChannel()
		sensor_volts = sensor.ConvertVolts(sensor_level,2)

		# Print out results to comand line
		print"---"
		if not debug:
			print("Data: {}".format(sensor_level))
		else:
			print("{} {} ({}V)".format(sensor.id_,sensor_level,sensor_volts))
		
		#write_line("{},{},{},{},{}\n".format(sensor.id_,sensor.type_,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),sensor_level,sensor_volts))

#open log.csv, write meta information and data from sensor, close document
def write_line(line):
	with open('log.csv','a') as f:
		f.write(line)
		f.close()

def main(): #function to time multiple events
	prev_milli_time_1 = int(round(time.time()*1000))
	prev_milli_time_2 = int(round(time.time()*1000))
	blink_interval = 100
	measure_interval = 0
	try:
		while True:
			if current_milli_time() - prev_milli_time_1 > blink_interval:	#Timer 
				prev_milli_time_1 = int(current_milli_time())
				blink_status()

				if led.getState():
					blink_interval = 100 #blink durration
				else:
					blink_interval = 2900 #interval between blinks

			if current_milli_time() - prev_milli_time_2 > measure_interval:	#Timer 
				prev_milli_time_2 = int(current_milli_time())
				measure()
				measure_interval = 2000	

	except Exception, e:
		raise
	else:
		pass
	finally:
		GPIO.cleanup()

main()