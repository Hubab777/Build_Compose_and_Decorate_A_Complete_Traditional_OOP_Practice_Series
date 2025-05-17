class TemperatureConvertor():
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
if __name__ == "__main__":
    print("Fahrenheit:", TemperatureConvertor.celsius_to_fahrenheit(3))
    print("Fahrenheit:", TemperatureConvertor.celsius_to_fahrenheit(12))
    