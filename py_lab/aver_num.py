#### 1.몇개의 숫자를 입력할것인지
print("how many numbers you're gonna enter? :",end=" ")
#### 2.갯수만큼 숫자 입력
tries = int(input());

n_list = []
print("numbers should be entered. ("+str(tries)+" times with space) : ",end="") 
num = input();
n_list = num.split(" ");
n_list= list(map(int,n_list))

#type(변수) - 자료형 확인


#### 3.갯수만큼 반복하며 입력된 숫자 모두 더함
n_sum = 0
for val in n_list :
    n_sum += val


#### 4.평균 계산
s = sum(n_list) / len(n_list)
n_sum /= tries
#### 5.평균 출력
print("The average of your numbers is ["+str(s)+"]")
#print("The average of your numbers is ["+str(n_sum)+"]")

# pause

import os
os.system("pause")
