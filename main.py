# Python object-oriented programming
import datetime


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # example of using class method as alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.5

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # alternative: Employee.__init__(first, last, pay)
        # but ^ less maintainable in the case of multiple inheritance
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

    def print_all_employees(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev1 = Developer("James", "Soo", 100000, "Python")
dev2 = Developer("Catherine", "Yi", 200000, "JavaScript")

manager1 = Manager("Mao", "Li", 1000000, [dev1])

print(issubclass(Employee, Developer))
