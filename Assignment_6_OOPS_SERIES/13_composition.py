
class Engine:
    def start(self):
        print("New Engine has been placed inside the car.")
        
class Car:
    def __init__(self):
        self.engine = Engine() # composition
        
    def start_car(self):
        self.engine.start()
        
if __name__ == "__main__":
    my_car = Car()
    my_car.start_car()
        