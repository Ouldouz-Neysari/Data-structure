
n=int(input())
arr=[0]*n

for i in range(n-1):
    temp=[int(element) for element in input().split()]
    arr[temp[0]-1]+=1
    arr[temp[1]-1]+=1


#print(arr)

def yes_no_det(arr):
    leaves_count=0
    for j in range(n):
        if(arr[j]==2):
            return 0
        if(arr[j]==1):
            leaves_count+=1
    if(leaves_count*(leaves_count-1)/2 >= n-1):
        return 1
    else:
        return 0

#print(leaves_count*(leaves_count-1)/2,n-1)
if(yes_no_det(arr)==1):
    print("YES")
else:
    print("NO")   