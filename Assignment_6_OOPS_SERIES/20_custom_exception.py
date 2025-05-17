#  Custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18."):
        self.message = message
        super().__init__(self.message)

# Function that uses the exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Access denied!")
    else:
        print("Access granted. Age is valid.")

# try...except to handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Caught an exception:", e)
except ValueError:
    print("Please enter a valid number.")
