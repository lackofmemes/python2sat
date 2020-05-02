# Applications of a Stack

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
    
    
# 1) Reverse a word using a stack
"""
word = "HelloWorld"
# Note you could just do it like this ---->   print(word[::-1])

my_stack = Stack()
for character in word:
    my_stack.push(character)
    
reverse_word = ""
while not my_stack.isEmpty():
    character = my_stack.pop()
    reverse_word = reverse_word + character
print(reverse_word)
"""

# 2) Have a undo feature for a game
circle_x = 100
circle_y = 100
num_of_moves = 0
my_locations = Stack()

def setup():
    size(700, 700)
    
    
def draw():
    global circle_x
    global circle_y
    # Clear previous frame
    background(0, 0, 0)
    
    # Draw the ball
    fill(255, 0, 0)
    ellipse(circle_x, circle_y, 50, 50)
    
def keyPressed():
    global circle_x
    global circle_y
    global num_of_moves
    global my_locations
    
    if key == "w":
        num_of_moves += 1
        circle_y = circle_y - 25
    elif key == "s":
        num_of_moves += 1
        circle_y = circle_y + 25
    elif key == "a":
        num_of_moves += 1
        circle_x = circle_x - 25
    elif key == "d":
        num_of_moves += 1
        circle_x = circle_x + 25
    elif key == "z":
        location = my_locations.pop()
        print(location)
        circle_x = location[0]
        circle_y = location[1]
        print(circle_x, circle_y)
        
    if num_of_moves == 5:
        num_of_moves = 0
        print((circle_x, circle_y))
        my_locations.push((circle_x, circle_y))
        
        
        
