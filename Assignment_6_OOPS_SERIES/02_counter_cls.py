class Counter:
    count = 0   # class variable
    
    def __init__(self):
        Counter.count += 1
        
    @classmethod
    def show_counter(cls):
        print(f"Total no of created objects: {cls.count}")
        
c1 = Counter()
c2 = Counter()
Counter.show_counter()