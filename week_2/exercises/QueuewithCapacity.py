from _typeshed import StrPath


class Queue:
    def __init__(self, max_size):
        self.list = [None] * max_size
        self.start = -1
        self.end = -1
        self.max_size = max_size

    def isFull(self):
        if self.end - self.startd == 1:
            return True
        if self.start == 0 and self.end == self.max_size -1:
            return True
        return False

    def isEmpty(self):
        if self.start == -1:
            return True
        return False

    def enqueue(self,value):
        if self.isFull():
            return "List is full"
        
        self.end = self.end + 1

        # if enqueueing to an empty list
        if self.isEmpty():
            self.start = 0
        elif self.end +1 == self.max_size:
            self.end =0
        else:
            self.end = self.end + 1
        self.list[self.end] = value

    def dequeue(self):
        if self.isEmpty():
            return "No element in the queue"
        value = self.list[self.start]

        if self.start + 1 == self.max_size:
            self.start = 0
        elif self.start == self.end:
            self.start = -1
            self.end = -1
        else:
            self.start = self.start + 1
        return value
    
    def peek(self):
        if self.isEmpty():
            return "No element in the queue"
        return self.list[self.start]

    def delete(self):
        self.list = [None] * self.max_size
        self.start = -1
        self.end = -1

        