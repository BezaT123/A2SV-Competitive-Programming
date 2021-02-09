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
        return self.list.pop()

    def peek(self):
        if not self.isEmpty():
            return self.list[len(self.list)-1]
    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.push(i)
            else:
                if stack.isEmpty():
                    return False
                if i == ')' and stack.peek() == '(':
                    stack.pop()
                elif i == '}' and stack.peek() == '{':
                    stack.pop()
                elif i == ']' and stack.peek() == '[':
                    stack.pop()
                else:
                    return False
        # print(stack.isEmpty())
        return stack.isEmpty()
        