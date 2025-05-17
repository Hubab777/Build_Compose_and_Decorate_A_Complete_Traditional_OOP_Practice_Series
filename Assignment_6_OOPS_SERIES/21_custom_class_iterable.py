class Countdown:
    def __init__(self, start):
        self.current = start  # store starting number

    def __iter__(self):
        return self  # the object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # stops the iteration when done
        else:
            value = self.current  # store current value to return
            self.current -= 1     # move to next (smaller) number
            return value
        
cd = Countdown(10)

for number in cd:
    print(number)
    
print("⏳ Countdown timer ended!")

