from gpib import *
from srs844 import *
from hp6653a import *
from hp8672a import *

import time

g = gpib.gpib()
#lia = srs844(g,3)
uwsource = hp8672a(g,3)
#psu = hp6653a(g,2)

#psu.set_voltage(4);
#psu.set_current(6);
#psu.set_output("off")

for i in xrange(15,20):
	print "Trying %i\n" % i
	uwsource = hp8672a(g,i)
	uwsource.set_frequency_mhz(7);
	time.sleep(1)