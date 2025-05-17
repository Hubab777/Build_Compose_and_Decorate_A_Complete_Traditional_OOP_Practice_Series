
def add_greeting(cls):
   
    def greet(self):
        print("Hello from Decorator!")
    
    def hello(self):
        print(f"Hello {self.name}! Have a great day.")
    
    cls.greet = greet
    cls.hello = hello

    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Mr.Uzair")
p.greet()
p.hello()  
