class SetofStacks:
    def __init__(self,capacity):
        self.capacity = capacity
        self.list = []
        self.indices = []

    def push(self, value):
        if self.isFull():
            self.indices.append(len(self.list) -1)
        self.list.append(value)

    def isFull(self):
        if len(self.list) == 0:
            return False
        if len(self.list) % self.capacity == 0:
            return True
        return False

    def pop(self):
        # value = self.list[len(self.list) -1]
        if len(self.list) % self.capacity == 1:
            self.indices.pop()
        return self.list.pop()

    def popAt(self,index):
        stack_number = len(self.list) // self.capacity
        if index > stack_number:
            return "No such stack"
        if index == stack_number:
            # Normal pop... pop from the last
            return self.pop()
        if index < stack_number:
            value = self.list[self.indices[index]]
            del(self.list[self.indices[index]])
            if self.indices[index] - 1 < 0:
                del(self.indices[index])
            else:
                self.indices[index] -= 1
            return value

custom_stack = SetofStacks(2)
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(4)
custom_stack.push(5)
print(custom_stack.popAt(0))
print(custom_stack.popAt(0))
custom_stack.push(6)
custom_stack.push(7)

print(custom_stack.list)
print(custom_stack.indices)

# 
