# Object-Oriented-Programing

**Lecture 1: Classes and instances of that class using example Employee**
__init__(self) method or aka constructor of a class. basically a base function of the class with its instance variables and a method in a class for full name

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
  
emp_1 = Employee('Simran', 'Chadha', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


**Lecture 2: Class variables**
class Employee:
  raise_amount = 1.04
  def __init__(self, first, last, pay):

  def apply_raise(self):
    self.pay = int(self.pay + self.raise_amount)



Lecture 3: Static methods and Class methods

adding a decorator (decorator lecture)

@classmethod

**Lecture 4: Inheritance - Subclass**

#useful help function

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)# to avoid redundancy
       # or Employee.__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()

isinheritance()
issubclass(Developer, Employee)

**Lecture 5- Dunder/Magic method**

__add__


__repr__
__str__




