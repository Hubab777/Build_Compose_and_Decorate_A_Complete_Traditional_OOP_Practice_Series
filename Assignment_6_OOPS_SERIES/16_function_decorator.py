
def log_function_call(func):
    def wrapper():
        print("Function is being called")  # Extra behavior
        return func()                      # Call the original function
    return wrapper                         # Return the wrapper function

@log_function_call
def say_hello():
    print("Hello!")

say_hello()
