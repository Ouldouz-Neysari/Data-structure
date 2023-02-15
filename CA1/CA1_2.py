import math

input_str=input()
count=0
for i in range(len(input_str)//2):
    if input_str[i]!=input_str[i*(-1)-1]:
        count+=1

steps=2**(count)
number=10**(9)+7
print(count,steps%(number))