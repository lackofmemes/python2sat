# Stack LIFO

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.isEmpty():
            return None
        
        return self.items.pop(-1)
    
    def size(self):
        return len(self.items)
    
my_stack = Stack()
print(my_stack.isEmpty())
my_stack.push(30)
my_stack.push(99)
print(my_stack.pop())
print(my_stack.size())
        
        
