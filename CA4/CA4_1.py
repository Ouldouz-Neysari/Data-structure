def path_finder(g_matrix,index,path_visited,num_of_nodes,is_path):

	this_node=index
	next_i=g_matrix[index][0]

	while True:
            num_of_nodes += 1
            path_visited[next_i] = True

            if len(g_matrix[next_i]) == 1: 
                if len(g_matrix[index]) == 1 or path_visited[g_matrix[index][1]] == True: 
                    is_path = True
                    break
                else:
                    this_node = index
                    next_i= g_matrix[index][1]
            elif g_matrix[next_i][0] == this_node and g_matrix[next_i][1] != index:
                this_node = next_i
                next_i = g_matrix[next_i][1]
            elif g_matrix[next_i][0] != index and g_matrix[next_i][1] == this_node:
                this_node = next_i
                next_i = g_matrix[next_i][0]
            else: 
                break

	return is_path,num_of_nodes





n,m= input().split()

arr=[[] for i in range(int(n))]

vertics_arr=[]
path_visited=[False]*int(n)
C=0
odd_paths=0

for i in range(int(m)):

	a,b=input().split()
	arr[int(a)-1].append(int(b)-1)
	arr[int(b)-1].append(int(a)-1)


for p in range(int(n)):
	if(path_visited[p]==False):
		path_visited[p]=True

		if(len(arr[p])==0):
			odd_paths+=1
			continue

		num_of_nodes=1
		is_path=False
		is_path,num_of_nodes=path_finder(arr,p,path_visited,num_of_nodes,is_path)

		if( num_of_nodes %2 )==1 and is_path==False:

			C+=1
		if( num_of_nodes %2 )==1 and is_path==True:

			odd_paths+=1

if (odd_paths %2)==1:
	C+=1


print(C)