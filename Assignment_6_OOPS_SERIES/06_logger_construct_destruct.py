class Logger:
    def __init__(self):
        print("Logger object has created!")
        
    def __del__(self):
        print("Logger object has destroyed!")
        
log = Logger()
del log