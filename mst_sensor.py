#class version of read_sensor.py
import time
import os
import spidev

class Sensor(object):


	def __init__(self, channel, debug):
		self.channel = channel
		self.debug = debug
		# Open SPI bus
		spi = spidev.SpiDev()
		spi.open(0,0)

	def ReadChannel(channel):
		adc = spi.xfer2([1,(8+channel)<<4,0])
		data = ((adc[1]&3) << 8) + adc[2]
		return data

	def ConvertVolts(data,places):
		volts = (data * 3.3) / float(1023)
		volts = round(volts,places)
		return volts