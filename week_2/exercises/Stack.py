class Stack:
    def __init__(self, list = []):
        self.list = list
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def push(self,value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "No element in the stack"
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "No element in the stack"
        return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None
    
    

stack = Stack([1,2,3,4])
print(stack.list)
stack.push(5)
print(stack.list)
stack.pop()
print(stack.list)

