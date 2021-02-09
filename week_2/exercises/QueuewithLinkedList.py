class Node:
    def __init__(self, value =0, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head
    def print_list(self):
        current = self.head
        while(current != None):
            print(current.value)
            current = current.next

class Queue:
    def __init__(self, linkedList = None):
        self.linkedList = linkedList

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
            return

        self.linkedList.tail.next = new_node
        self.linkedList.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            return "No elements in the queue"
        
        value = self.linkedList.head.value
        if self.linkedList.head == self.linkedList.tail:
            self.linkedList.tail = None
            
        self.linkedList.head = self.linkedList.head.next
        return value
    
    def peek(self):
        if self.isEmpty():
            return "No elements in the queue"
        return self.linkedList.head.value

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
