import copy


def new_array(arr,c):
    new_arr=[]
    prev=arr.copy()
    temp=[]
    prev=arr
    for i in range(c):
        for element in prev:
            temp.append(prev.count(element))
            #temp.append(dup_finder(prev,element=element))
        prev=temp[:]
        new_arr.append(prev)
        temp.clear()
    return new_arr
    
n,q=input().split()
input_array=input()
num_array=[int(element) for element in input_array.split()]
c_list=[]
d_list=[]
max,d=input().split()
c_list.append(int(max))
d_list.append(int(d))

for i in range(int(q)-1):
    c,d=input().split()
    if(int(c)>int(max)):
        max=c
    c_list.append(int(c))
    d_list.append(int(d))


complete_arr=new_array(num_array,int(max))
for j in range(int(q)):    
    print(complete_arr[c_list[j]-1][d_list[j]-1])

