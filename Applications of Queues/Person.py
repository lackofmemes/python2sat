class Person:
    def __init__(self, name, gender, age, health_num):
        self.name = name
        self.gender = gender
        self.age = age
        self.health_num = health_num

    def __str__(self):
        return self.name + ":[" + self.health_num + "]"

        
