class Employee:
    raise_amt = 1.4
    no_of_emps = 0

    def __init__(self, first, last, salary=None):
        self.first = first
        self._last = last
        self.__salary = salary
        self.email = f"{self.first}.{self._last}@company.com"

        Employee.no_of_emps += 1

    def __mro_entries__(self, bases):
        pass

    def __str__(self):
        return f"Employee('{self.first}', '{self._last}', {self.__salary})"

    @classmethod
    def from_string(cls, emp_str: str):
        first, last, salary= emp_str.split("-")
        return cls(first, last, salary)

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):
        self._last = last

    @property
    def salary(self):
        return self.__salary


emp1 = Employee("Pradeep", "Ramola", 10000)
emp2 = Employee("John", "Lennon", 20000)
emp_string = "Black-Smith-30000"
emp3 = Employee.from_string(emp_string)
print(emp3)
print(emp3.salary)
emp3.last = "saini"
print(emp3.last)
