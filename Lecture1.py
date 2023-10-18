class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
  
emp_1 = Employee('Simran', 'Chadha', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)