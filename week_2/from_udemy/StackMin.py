class Stack:
    def __init__(self,list =[]):
        self.list = list
        self.min_list = []

    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def pop(self):
        if self.list == []:
            return "Stack is Empty"
        if self.peek() == self.min():
            del(self.min_list[len(self.min_list) - 1])
        return self.list.pop()

    def push(self,value):
        if self.list == []:
            self.min_list.append(value)
        elif self.min() >=value:
            self.min_list.append(value)
        self.list.append(value)

    def peek(self):
        return self.list[len(self.list) - 1]
    
    def min(self):
        return self.min_list[len(self.min_list) - 1]


stack = Stack()
# stack.push(-2)
# stack.push(0)
stack.push(-3)
# stack.push(0)
print(stack.list)
print(stack.min_list)
print(stack.min())
# stack.pop()
# print(stack.list)
# print(stack.min_list)

# stack.pop()
# print(stack.list)
# print(stack.min_list)

# stack.pop()
# print(stack.list)
# print(stack.min_list)

# stack.pop()
# print(stack.list)
# print(stack.min_list)