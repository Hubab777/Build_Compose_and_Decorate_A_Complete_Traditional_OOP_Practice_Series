
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"My name is {self.name} & I secured {self.marks} marks!")
        
s1 = Student("Hubab", 98)
s1.display()