class Queue:
    def __init__(self, list = []):
        self.list = list
    def enqueue(self,value):
        self.list.append(value)
    def dequeue(self):
        if self.isEmpty():
            return "No elements in the queue"
        return self.list.pop(0)
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    def peek(self):
        return self.list[0]
    def delete(self):
        self.list = None
    
    
queue = Queue([1,2,3,4])
queue.enqueue(5)
print(queue.list)
queue.dequeue()
print(queue.list)