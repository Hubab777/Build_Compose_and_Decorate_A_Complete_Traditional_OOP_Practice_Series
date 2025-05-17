class Car:
    def __init__(self, brand):
       self.brand = brand
       
    def start(self): 
        print(f"{self.brand} is operational from now onwards")
        
my_car = Car("Tesla")
print(my_car.brand)
my_car.start()