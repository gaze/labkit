import gpib
import time

class srs844():

	def __init__(self,gpib,addr):
		self.gpib=gpib
		self.addr=addr

		self.gpib.set_addr(addr);
		self.gpib.write("*CLS");  # clear all status regs
		self.gpib.write("OUTX1"); # Out gpib

		self.gpib.write("*RST");
		self.gpib.write("REST");
		
		time.sleep(3)
		
		self.gpib.write("*IDN?");
		print self.gpib.read();
		

	def get_point(self):
		print "Getting point"
		self.gpib.set_addr(self.addr);
		self.gpib.write("SNAP?1,2,3,5");
		print self.gpib.read();
		