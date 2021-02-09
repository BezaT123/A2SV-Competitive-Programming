class Node:
    def __init__(self, value =0, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head
        self.size = 0 if head == None else 1
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def insert(self, value,location):
        new_node = Node(value)
        # inserting at an empty linked list
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            # inserting at the beginning
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.size += 1


            # inserting at the end
            elif location == -1 :
                self.tail.next = new_node
                self.tail = new_node
                self.size += 1

            # inserting at a given location
            else:
                index = 0
                current = self.head
                while index < location - 1:
                    current = current.next
                    index += 1
                new_node.next = current.next
                current.next = new_node
                self.size += 1

    def get(self, index):
        if index == 0:
            return self.head.value
        if index >= self.size:
            return -1
        if index == self.size - 1:
            return self.tail.value
        indx = 0
        current = self.head
        while indx < self.size:
            if indx == index:
                return current.value
            current = current.next
            indx += 1
    
    def delete(self,nodeValue):
        if self.head == self.tail and self.head.value == nodeValue:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        if self.head.value == nodeValue:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = prev = self.head
        while current:
            if current.value == nodeValue:
                break
            prev = current
            current = current.next
        if current == self.tail:
            prev.next = None
            self.tail = prev
            
        else:
            prev.next = current.next
        self.size -= 1

    

    



sLL = LinkedList()
sLL.insert(1,0)
# print(sLL.tail)
sLL.insert(2,-1)
sLL.insert(3,0)
sLL.insert(4,-1)
sLL.insert(5,3)
sLL.insert(8,-1)
sLL.insert(9,3)

sLL.print_list()
print()
sLL.delete(9)
sLL.print_list()
