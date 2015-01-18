# main
import time
from mst_sensor import Sensor
from rgb import RGB 

debug = True
delay = 1

rgb = RGB(23,24,25,debug)
sensor = Sensor(0, debug)

while True:

        # Read the sensor data
        sensor_level = sensor.ReadChannel()
        sensor_volts = sensor.ConvertVolts(sensor_level,2)

        # Print out results
        print"---"
        if debug:
                print("Data: {}".format(sensor_level))
        else:
                print("Data: {} ({}V)".format(sensor_level,sensor_volts))

        # Wait before repeating loop
        time.sleep(delay)