class Employee:
    def __init__(self, name):
        self.name = name
        
class Department:
    def __init__(self, employee):
       self.employee = employee
       
    def show_employee(self):
        print(f"Employee currently working in department: {self.employee.name}") 
        
if __name__ == "__main__":
    emp = Employee("Farheen")
    dept = Department(emp)  # aggregation
    dept.show_employee()
    