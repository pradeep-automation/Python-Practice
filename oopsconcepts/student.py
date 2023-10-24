class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.grade})"


class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False


s1 = Student("Pradeep", 34, 80)
s2 = Student("Kuldeep", 37, 85)
s3 = Student("Sandeep", 40, 90)
print(s1)

c1 = Course("Python", 2)
print(c1.add_student(s1))
print(c1.add_student(s2))
print(c1.add_student(s3))
print(c1.students)



