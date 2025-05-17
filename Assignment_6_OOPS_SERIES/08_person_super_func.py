class Person:
    def __init__(self, name):
        self.name = name
        
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
t1 = Teacher("Zarlish", "Research Work")
print(t1.name, "& her", t1.subject,"!")
print(f"{t1.name} is doing some {t1.subject} which is her passion.")
    