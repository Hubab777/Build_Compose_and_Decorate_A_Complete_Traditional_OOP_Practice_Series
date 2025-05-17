class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} says Woof Woof!")
        print(f"{self.name} belongs to {self.breed} breed.")
        
my_dog = Dog("Rex", "Labrador")

my_dog.bark()
