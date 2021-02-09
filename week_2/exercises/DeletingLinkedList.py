class Node:
    def __init__(self, value =0, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def delete_node(self, node):
        #deleting from the head
        if node == self.head:
            self.head = node.next
            return

        #deleting from the any given
        prev = self.head
        while(prev != None):
            if prev.next == node:
                prev.next = node.next
                break
            # print(current.value)
            prev = prev.next
    
    def print_list(self):
        current = self.head
        while(current != None):
            print(current.value)
            current = current.next
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
singlyLinkedList = LinkedList(a)

# singlyLinkedList.delete_node(a)
singlyLinkedList.print_list()

# print(head.value)