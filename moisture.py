# main
import threading
import time
from mst_sensor import Sensor
from rgb import RGB 

debug = True
delay = 1

sensor = Sensor(0, debug)

blink = RGB(23,24,25,debug,0.1,1)
# print threading
blink.start()
print "Started blinking"

#if debug:
#	rgb.blink("Blue",0.1,10)
#else:
#	rgb.blink("Green",0.1,1)

while True:

        # Read the sensor data
        sensor_level = sensor.ReadChannel()
        sensor_volts = sensor.ConvertVolts(sensor_level,2)

        # Print out results
        print"---"
        if not debug:
                print("Data: {}".format(sensor_level))
        else:
                print("Data: {} ({}V)".format(sensor_level,sensor_volts))

        # Wait before repeating loop
        time.sleep(delay)
        