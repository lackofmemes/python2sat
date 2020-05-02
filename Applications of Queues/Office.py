from Queue import *

class Office:
    def __init__(self, name, type_of_office):
        self.name = name
        self.type = type_of_office
        self.queue = Queue()

    def add_patient(self, person):
        self.queue.enqueue(person)

    def get_next_patient(self):
        if self.queue.isEmpty():
            return -1  # -1 means no body in line
        
        return self.queue.dequeue()

    def get_number_of_patients(self):
        return self.queue.size()

    def __str__(self):
        return_str = self.name + "\n"
        temp = self.queue.items
        for person in temp:
           return_str += str(person) + "\n"
        return return_str
    
