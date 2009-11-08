import os
import serial
import time
from struct import *

class gpib():
	def __init__(self):
		# Switch for OS X
		# self.serial = serial.Serial('/dev/ttyUSB%d'%usbnumber,rtscts=0,timeout=1)
		self.serial = serial.Serial('/dev/tty.usbserial-PXR9GXN3',rtscts=0,timeout=1)
		
		self.writeser('++mode 1'+"\r")
		time.sleep(0.1)
		self.writeser('++ifc'+"\r")
		time.sleep(0.1)
		self.writeser('++auto 0'+"\r")
		time.sleep(0.1)
		self.writeser('++eoi 0'+"\r")
		time.sleep(0.1)
		self.caddr = -1
		
	def set_addr(self,addr):
		if(self.caddr != addr):
			self.writeser('++addr '+str(addr)+"\r")
			time.sleep(0.1)
			self.caddr=addr
		
	def read(self):
		self.writeser('++read eoi'+"\r")
		return self.serial.readline()
		
	def write(self,gpibstr):
		self.writeser(gpibstr+"\r")
	
	def writeser(self, str):
		print "DEBUG: %s" % str
		self.serial.write(str);
