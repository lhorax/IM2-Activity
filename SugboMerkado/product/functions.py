#contains all my methods regarding this app

import math

#method for displaying SKU
def getSku(id):
	t1 = math.floor(id/26000)%26
	t2 = math.floor(id/1000)%26
	t3 = math.floor(id/100)%10
	t4 = math.floor(id/10)%10
	t5 = math.floor(id%10)
	f = chr(t1 + 65)
	s = chr(t2 + 65) 
	t = chr(t3 + 48)
	fo = chr(t4 + 48)
	fi = chr(t5 + 48)
	return ('P'+f+s+t+fo+fi)