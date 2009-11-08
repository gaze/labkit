class hp8672a():
	def __init__(self, gpib, addr):
		self.gpib = gpib
		self.addr = addr

	def set_frequency_mhz(self,mhz):
		self.gpib.set_addr(self.addr)
		self.gpib.write("P%04iZ0" % mhz);