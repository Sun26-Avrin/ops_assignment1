#!/usr/bin/python

import my_pkg.Tobinary
import my_pkg.union

while(1) :
	menu = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ? "))

	if (menu == 1) :
		a = input("input binary number : ")
		my_pkg.Tobinary.bin_to_all(a)

	if (menu == 2) :
		a = input("1st list: ")
		b = input("2nd list: ")
		token = [",", "[", "]"]
		for tok in token : 
			a= a.replace(tok," ")
			b= b.replace(tok," ")
		li_a=list(map(int,a.split()))
		li_b=list(map(int,b.split()))
		my_pkg.union.uni(li_a,li_b)

	if (menu == 3) :
		break
	
