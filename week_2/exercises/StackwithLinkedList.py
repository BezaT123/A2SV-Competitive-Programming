class Node:
    def __init__(self, value =0, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    def print_list(self):
        current = self.head
        while(current != None):
            print(current.value)
            current = current.next

class Stack:
    def __init__(self, linkedList = None):
        self.linkedList = linkedList
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        return False
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.linkedList.head
        self.linkedList.head = new_node

    def pop(self):
        if self.isEmpty():
            return "No element in the stack"
        value = self.linkedList.head.value
        self.linkedList.head = self.linkedList.head.next
        return value

    def peek(self):
        if self.isEmpty():
            return "No element in the stack"
        return self.linkedList.head.value
    
    def delete(self):
        self.linkedList.head = None
    
    
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
singlyLinkedList = LinkedList(a)

stack = Stack(singlyLinkedList)
# print(stack.list)
stack.linkedList.print_list()
print()
stack.push(5)
# print(stack.list)
stack.linkedList.print_list()
print()

stack.pop()
# print(stack.list)
stack.linkedList.print_list()


