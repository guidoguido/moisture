#!/usr/bin/python
import time
import os
import spidev
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
DEBUG = 1


# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
        adc = spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
        volts = (data * 3.3) / float(1023)
        volts = round(volts,places)
        return volts

sensor_channel = 0

# Define delay between readings
delay = 2

while True:

        # Read the sensor data
        sensor_level = ReadChannel(sensor_channel)
        sensor_volts = ConvertVolts(sensor_level,2)

        # Print out results
        print"---"
        if DEBUG == 0:
                print("Data: {}".format(sensor_level))
        else:
                print("Data: {} ({}V)".format(sensor_level,sensor_volts))

        # Wait before repeating loop
        time.sleep(delay)