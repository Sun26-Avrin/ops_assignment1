#!/usr/bin/python

#-*- coding:euc-kr -*-



while(1) :
    print("how many numbers you're gonna enter? :")
    
    tries = int(input())
    n_list=[]
    print("numbers should be entered. ("+str(tries)+" times with space) : ")
    num=input()
    n_list = num.split(" ")
    #loop
    if(len(n_list) != tries) :
        print("You've typed wrong number of numbers")
        continue
    else :
        break

n_list=list(map(int,n_list))


n_sum=0
for val in n_list :
    n_sum +=val


n_sum /= tries
s = sum(n_list)/len(n_list)

print("The average of your numbers is ["+str(n_sum)+"]")

    
