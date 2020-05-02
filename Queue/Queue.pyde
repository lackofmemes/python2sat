# Queue FIFO

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            return None
        
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
my_q = Queue()
print(my_q.isEmpty())
my_q.enqueue(30)
my_q.enqueue(99)
print(my_q.dequeue())
print(my_q.size())
    
