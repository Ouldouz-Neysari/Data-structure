class MinHeap:
    def __init__(self):
        self.elements = []
        self.NOE = 0
    def sift_up(self, i):
        end_index = self.NOE
        start_index = i
        new_element = self.elements[i]
    
        left_child_index = 2*i + 1  
        while left_child_index < end_index:
        
            right_child_index = left_child_index + 1
            if right_child_index < end_index and not self.elements[left_child_index] < self.elements[right_child_index]:
                left_child_index = right_child_index
        
            self.elements[i] = self.elements[left_child_index]
            i = left_child_index
            left_child_index = 2*i + 1
        self.elements[i] = new_element
        self.bubble_down( start_index, i)




    def bubble_down(self, start_index,new_element_index):
        new_element = self.elements[new_element_index]

        while new_element_index > start_index:
            parent_index= (new_element_index - 1) >> 1
            parent = self.elements[parent_index]
            if new_element < parent:
                self.elements[new_element_index] = parent
                new_element_index = parent_index
                continue
            break
        self.elements[new_element_index]= new_element

                

  
    def insert(self, new_element):
        self.elements.append(new_element)
        self.NOE+=1
        self.bubble_down(0, self.NOE-1)

    def remove(self):
        last_element = self.elements.pop()  
        self.NOE-=1 
        if self.elements:
            r_value= self.elements[0]
            self.elements[0] = last_element
            self.sift_up(0)
            return r_value
        return last_element

    def poshtak_arranger(self,sum):
        a=self.remove()
        b=self.remove()
        self.insert(a+b)
        sum+=a+b
        return sum


n=int(input())
arr=[int(element) for element in input().split()]
my_Heap=MinHeap()
for i in range(n):
    my_Heap.insert(arr[i])
sum=0
for j in range(n-1):
    sum=my_Heap.poshtak_arranger(sum)


print(sum)