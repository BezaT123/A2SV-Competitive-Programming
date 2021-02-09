class Node:
    def __init__(self,value = None, next = None):
        self.value = value
        self.next = next

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        self.min = None

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node2 = Node(x)
        if self.head == None or self.getMin() >= x:
            self.min = Node(value = x,next = self.min)
        self.head = Node(value = x,next = self.head)

    def pop(self) -> None:
        value = self.top()
        if value == self.getMin():
            self.min = self.min.next
        self.head = self.head.next
        return value

    def top(self) -> int:
        return self.head.value

    def getMin(self) -> int:
        return self.min.value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()