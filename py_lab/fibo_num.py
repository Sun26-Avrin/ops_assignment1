#!/usr/bin/python

#-*- coding:utf-8 -*-
print("Type the number to make Fibonacci sequence  : ")
tries = int(input())

fibo_list=[]
f3=0

for n in range(tries+1) :
	if(n==0) :
		continue
	elif(n==1 or n==2) :
		fibo_list.append(1)
	else :
		f3 = fibo_list[n-3]+fibo_list[n-2]
		fibo_list.append(f3)

print("Printing Fibonacci sequence...")
print(fibo_list)

print("Printing Fibonacci number...")
print("F("+str(tries)+") = "+str(fibo_list[-1]))
