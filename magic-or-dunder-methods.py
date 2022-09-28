class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}' )".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __sub__(self, other):
        return self.pay - other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee("Jimmy", "B", 3000)
emp2 = Employee("Jimmy", "C", 5000)

print(emp1.__repr__())
# same as
print(repr(emp1))

print(emp1 + emp2)
print(emp1 - emp2)

print("length of employee name without space:", len(emp2))
