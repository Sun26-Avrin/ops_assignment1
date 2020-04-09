#### 1.생성할 피보나치 수열의 갯수 입력
print("생성할 피보나치 수열의 갯수(n)를 입력하세요 : ",end="")
tries = int(input())
#### 2.피보나치 수열 출력
fibo_list = []
f3=0
for n in range(tries+1) :
    if(n==0) :
        continue
    elif(n==1 or n==2) :
        fibo_list.append(1)
    else :
        f3 = fibo_list[n-3]+fibo_list[n-2]
        fibo_list.append(f3)
        
print("피보나치 수열을 출력합니다...")
print(fibo_list)

#### 3.Fn 피보나치 수 출력
print("피보나치 수를 출력합니다...")
print("F("+str(tries)+") = "+str(fibo_list[-1]))


import os
os.system("pause")
