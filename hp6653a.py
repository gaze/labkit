class hp6653a():
	def __init__(self, gpib, addr):
		self.gpib = gpib
		self.addr = addr

	def set_voltage(self,voltage):
		self.gpib.set_addr(self.addr)
		self.gpib.write("VOLT %f" % voltage);
	
	def set_current(self,current):
		self.gpib.set_addr(self.addr)
		self.gpib.write("CURR %f" % current);
	
	def set_output(self,status):
		self.gpib.set_addr(self.addr)
		self.gpib.write("OUTP %s" % status);
