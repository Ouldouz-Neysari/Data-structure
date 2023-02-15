




def fix_root_distances(q,root_distances,fathers_arr,children_arr):
	while( q !=[]):
		a=q.pop(0)

		dis_val=root_distances[a]
		for ch in children_arr[a]:
			root_distances[ch]=dis_val+1
			q.append(ch)

def fix_next_gens(gen_q,next_gens,child_num,fathers_arr,children_arr,gen_checked):

	while ( gen_q !=[]):

		a=gen_q.pop(0)

		gen_val=next_gens[a]
		this_father=fathers_arr[a]

		if(child_num[a] ==1):
			continue
		else:

			#temp_vert=a
			while(this_father != -1 and child_num[this_father]==1):

				next_gens[this_father]+=gen_val

				gen_val=next_gens[this_father]

				this_father=fathers_arr[this_father]

				
			if (this_father !=-1):

				next_gens[this_father]+=gen_val
				child_num[this_father]=child_num[this_father]-1

				if(gen_checked[this_father]==0):

					gen_q.append(this_father)
					gen_checked[this_father]=1




n=int(input())


fathers_arr=[-1]
temp_arr=[int(x) for x in input().split()]

for i in range(n-1):
	fathers_arr.append(temp_arr[i]-1)


children_arr=[[] for i in range(int(n))]

for j in range(1,n):

	children_arr[fathers_arr[j]].append(j)


child_num=[len(children_arr[m]) for m in range(n)]


root_distances=[1]*n
next_gens=[1]*n

q=[0]

gen_q=[]

gen_checked=[0]*n

for k in range(n):
	if len(children_arr[k])==0:
		gen_q.append(k)

fix_root_distances(q,root_distances,fathers_arr,children_arr)

fix_next_gens(gen_q,next_gens,child_num,fathers_arr,children_arr,gen_checked)



print("1.0",end=" ")

for l in range(1,n):
	print((n-next_gens[l]+root_distances[l]+1)/2,end=" ")





