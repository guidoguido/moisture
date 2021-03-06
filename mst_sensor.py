#class version of read_sensor.py
import time
import os
import spidev

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

class Sensor(object):
	def __init__(self,id_,type_,channel,debug):
		self.id_ = id_
		self.type_ = type_
		self.channel = channel
		self.debug = debug
		
	def ReadChannel(self):
		adc = spi.xfer2([1,(8+self.channel)<<4,0])
		data = ((adc[1]&3) << 8) + adc[2]
		return data

	def ConvertVolts(self,data,places):
		volts = (data * 3.3) / float(1023)
		volts = round(volts,places)
		return volts