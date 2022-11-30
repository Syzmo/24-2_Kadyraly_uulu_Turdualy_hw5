class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"{self.fullname} \n{self.age}\n{self.is_married}")

    def __str__(self):
        return f"Name:{self.fullname}\n" \
               f"Age:{self.age}\n" \
               f"Marriage:{self.is_married}\n"
person1 = Person("Aman", "17", "no")
print(person1)
person2 = Person("Tasia", "22", True)
print(person2.introduce_myself())


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def averege(self):
        print(sum(self.marks) // len(self.marks))


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience=3):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 10000

    def teacher_cash(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary / 100 * 5) * (self.experience - 3))
            return new_salary

k = Teacher("aigerim", "yes", True, 10)
print(f"{k.fullname},{k.salary},{k.age},{k.is_married}")
print(k.teacher_cash())


def create_students():
    student1 = Student("Dan", 13, False, marks={
        "история": 2,
        "алгебра": 5,
        "физра": 3,
        "физика": 4,
        "химия": 5
    })
    student2 = Student("Ben", 15, False, marks={
        "история": 4,
        "алгебра": 5,
        "физра": 4,
        "физика": 4,
        "химия": 5
    })
    student3 = Student("Alex", 25, True, marks={
        "история": 5,
        "алгебра": 3,
        "физра": 5,
        "физика": 4,
        "химия": 5
    })

    result = [student1, student2, student3]
    return result


student = create_students()
for i in student:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name:{i.fullname}\n"
          f"Age:{i.age}\n"
          f"Marriage:{i.is_married}\n"
          f"Average:{sum(list) / len(list)}\n")
