class Employee:
    total_employee = 0

    def __init__(self,name,salary):
        self.employee_name = name
        self.employee_salary = salary
        Employee.total_employee += 1

    def display_employee(self):
        print(self.employee_name + " " + str(self.employee_salary))

    def display_count(self):
        print(Employee.total_employee)

#Creating object
emp1 = Employee("Jack", 24000)
emp1.display_employee()

emp2 = Employee("hgadg", 148100)
emp2.display_employee()
emp1.display_count()
