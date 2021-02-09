class Heap:
    def __init__(self):
        self.list = []
        
    def insert(self,value):
        # append to the last
        self.list.append(value)
        
        #heapify
        self.helper_up_heap(len(self.list)-1)
        
    def pop(self):
        # swap the last with root
        self.list[0] , self.list[len(self.list) - 1] = self.list[len(self.list) - 1] , self.list[0]
        # print(self.list)
        # size = len(self.list)-1

        #delete the last element
        val = self.list.pop(len(self.list) - 1)
        # print(self.list)

        # heapify
        self.helper_down_heap(0)
        return val

    def helper_up_heap(self,index):
        if index == 0:
            return
        # check with parent and swap
        parent = (index - 1) // 2
        # print(parent, index, self.list[index])

        if self.list[index] < self.list[parent]:
            self.list[index] , self.list[parent] = self.list[parent] , self.list[index]
            self.helper_up_heap(parent)

    def helper_down_heap(self,index):

        if 2 *index +1 >= len(self.list):
            return
        # print(index)
        min_index = 2 *index +1
        if 2 * index +2 < len(self.list):
            if self.list[2 * index + 1] >= self.list[2 *index +2]:
                min_index = 2 *index +2

        if self.list[index] > self.list[min_index]:
            self.list[index] , self.list[min_index] = self.list[min_index] , self.list[index]
            self.helper_down_heap(min_index)
        
heap = Heap()   
heap.list = []
# heap.insert(11)    
# # print(heap.list)
# heap.insert(2)    
# # print(heap.list)
# heap.insert(0)    
# # print(heap.list)
# heap.insert(1)    
# # print(heap.list)
# heap.insert(-2) 
# heap.insert(22)    
# heap.insert(6)   
     
# heap.list =[6,11,22]
# heap.pop()
# print(heap.list)
# heap.pop()
# print(heap.list)

l= []
heap.list = [-2,0,-1,11,1,22,6]
for i in range(len(heap.list)):
    l.append(heap.pop())


print(l)
# heap.list = [2,0,6,11,1,22]
# heap.helper_heapify(len(heap.list)//2)
# print(heap.list)