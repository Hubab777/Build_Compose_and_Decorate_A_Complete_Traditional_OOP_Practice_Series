class Multiplier:
    def __init__(self, factor):
         if factor == 0:
            raise ValueError("Factor cannot be zero!")
         self.factor = factor  

    def __call__(self, num):
        return num * self.factor  # Multiply input by the factor

multiply_by_3 = Multiplier(4)

print(callable(multiply_by_3)) 

# Call the object like a function
result = multiply_by_3(7)  # This will call the __call__() method
print(result) 
