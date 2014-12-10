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

light_channel = 0
#temp_channel  = 1

# Define delay between readings
delay = 2

while True:

        # Read the light sensor data
        light_level = ReadChannel(light_channel)
        light_volts = ConvertVolts(light_level,2)

        # Print out results
        print"---"
        if DEBUG == 0:
                print("Light: {}".format(light_level))
        else:
                print("Light: {} ({}V)".format(light_level,light_volts))

        # Wait before repeating loop
        time.sleep(delay)