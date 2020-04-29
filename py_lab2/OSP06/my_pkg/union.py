
def uni(li_a,li_b) :
	set_a = set(li_a)
	set_b = set(li_b)
	un1 = list((set_a | set_b))
	in1 = list((set_a & set_b))
	un1.sort()
	in1.sort()
	print("union : "+str(un1))
	print("intersection : "+str(in1))