class MultiStack:
    def __init__(self, stackSize):
        self.numberofStack = 3
        self.stackSize = stackSize
        self.list = [None] * (self.stackSize * self.numberofStack)
        self.sizes = [0] * self.numberofStack

    def indexOfTop(self,stackNumber):
        return ((stackNumber + 1) * self.stackSize ) - 1
    
    def indexOfBottom(self,stackNumber):
        return stackNumber * self.stackSize

    def isFull(self,stackNumber):
        # last_element = self.list[self.indexOfTop(stackNumber)]
        # if last_element is None:
        #     return False
        # return True
        if self.sizes[stackNumber] == self.stackSize:
            return True
        return False 
    
    def isEmpty(self,stackNumber):
        # first_element = self.list[self.indexOfBottom(stackNumber)]
        # if first_element is None:
        #     return True
        # return False
        if self.sizes[stackNumber] == 0:
            return True
        return False
    
    def push(self,stackNumber, value):
        if self.isFull(stackNumber):
            return "Stack" + str(stackNumber) + " is Full"
        self.list[self.indexOfBottom(stackNumber) + self.sizes[stackNumber]] = value
        self.sizes[stackNumber] += 1

    def pop(self, stackNumber):
        if self.isEmpty(stackNumber):
            return "Stack" + str(stackNumber) + " is Empty"
        value = self.list[self.indexOfBottom(stackNumber) + (self.sizes[stackNumber] - 1)]
        self.list[self.indexOfBottom(stackNumber) + (self.sizes[stackNumber] - 1)] = None
        self.sizes[stackNumber] -=1
        return value

    def peek(self,stackNumber):
        if self.isEmpty(stackNumber):
            return "Stack" + str(stackNumber) + " is Empty"
        return self.list[self.indexOfBottom(stackNumber) + self.sizes[stackNumber] - 1]



# please give me stackNumber with a zero index... start from zero
mStack = MultiStack(3)
print(mStack.list)
mStack.push(0,0)
mStack.push(1,4)
mStack.push(2,7)
print(mStack.list)

mStack.push(0,0)
mStack.push(1,4)
mStack.push(2,7)
print(mStack.list)

mStack.push(0,0)
mStack.push(1,4)
mStack.push(2,7)
print(mStack.list)

print(mStack.pop(1))

print(mStack.list)

print(mStack.peek(1))
print(mStack.isEmpty(0))


print(mStack.list)

