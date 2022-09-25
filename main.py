# Python object-oriented programming


class Employee:
    age = 100

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Kiefer", "Soon", 100000)
emp_2 = Employee("Carin", "Yee", 200000)

print(emp_1.fullname())
print(Employee.fullname(emp_2))
