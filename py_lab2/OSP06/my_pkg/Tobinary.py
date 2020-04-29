

def bin_to_all(a) :
	val = int(a,2)
	print("입력된값 : "+a)
	o=format(val,'o')
	d=val
	h=format(val,'x')
	print("OCT> "+str(o))
	print("DEC> "+str(d))
	print("HEX> "+str(h).upper())