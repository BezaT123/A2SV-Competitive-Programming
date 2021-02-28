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
        
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = Stack()
        max = 0
        count = 0
        
        for i in s:
            if i == '(':
                stack.push(i)
                count += 1
            if i == ')':
                stack.pop()
                if count > max:
                    max = count
                count -= 1

        return max