class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name   #public access modifier
        self._salary = salary  # protected access modifier
        self.__ssn = ssn  # private access modifier
        
emp = Employee("Hira", 60000, "03178930562")

print(emp.name)
print(emp._salary)
# print(emp.__ssn)
print(emp._Employee__ssn)
    