class BSTNode:
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.val = key
        self.weaker_children_num=0

def insert(root,v):
    if(root==None):
        return BSTNode(v)
    elif (root.val < v):

        root.right=insert(root.right,v)
    elif (root.val > v):
        root.weaker_children_num+=1
        root.left =insert(root.left,v)
    return root

def size(bst_node):
    if bst_node is None:
        return 0
    else:
        return (size(bst_node.left)+ 1 + size(bst_node.right))

def count_weakers(root,power):
    if(root==None):
        #print("aa")
        return 0
    else:
        #print(root)
        if(root.val==power):
            #print("qq")
            return root.weaker_children_num
        elif(root.val < power):
            #print(root.weaker_children_num)
            return root.weaker_children_num + 1 + count_weakers(root.right,power)
        else:
            #print("rr")
            return count_weakers(root.left,power)

q=int(input())
command_arr=[]
my_root=None

for j in range(q):
    command,num=input().split()
    command_arr.append([command,num])

for i in range(q):
    #command,num=input().split()
    if(command_arr[i][0]=="1"):
        my_root=insert(my_root,int(command_arr[i][1]))

    elif(command_arr[i][0]=="2"):
        #print(my_root.val)
        #print(my_root.right.val)
        print(count_weakers(my_root,int(command_arr[i][1])))


            
