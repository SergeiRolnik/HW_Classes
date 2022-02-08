class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
            course in lecturer.courses_attached and \
            (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Произошла ошибка. Оценка не выставлена.')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n\
Средняя оценка за домашние задания: {average_grade(self)}\n\
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n\
Завершенные курсы: {", ".join(self.finished_courses)}'

    def __gt__(self, other):
        return average_grade(self) > average_grade(other)

    def __lt__(self, other):
        return average_grade(self) < average_grade(other)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self)}'

    def __gt__(self, other):
        return average_grade(self) > average_grade(other)

    def __lt__(self, other):
        return average_grade(self) < average_grade(other)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and \
        (course in student.courses_in_progress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Произошла ошибка. Оценка не выставлена.')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def show_average_student_grade(student_list, course):
    grades_count = {}
    for student in student_list:
        if (course in student.courses_in_progress or course in student.finished_courses) and student.grades.keys():
            grades_count[student] = sum(student.grades[course]) / len(student.grades[course])
    return grades_count

def show_average_lecturer_grade(lecturer_list, course):
    grades_count = {}
    for lecturer in lecturer_list:
        if course in lecturer.courses_attached and lecturer.grades.keys():
            grades_count[lecturer] = sum(lecturer.grades[course]) / len(lecturer.grades[course])
    return grades_count

def average_grade(person):
    grades_list = []
    for course in person.grades.keys():
        grades_list += person.grades[course]
    if len(grades_list):
        return sum(grades_list) / len(grades_list)
    else:
        return 0

student_list = []
lecturer_list = []
# --------- REVIEWER
reviewer_1 = Reviewer('John', 'Wayne')
reviewer_1.courses_attached += ['Python', 'Java']
print("reviewer_1 data structure:", reviewer_1.__dict__)

# ---------- STUDENT LIST
student_1 = Student('Adam', 'Smith', 'Male')
student_1.courses_in_progress += ['Python', 'C++']
student_1.finished_courses += ['Java']
student_2 = Student('Kate', 'Parker', 'Female')
student_2.courses_in_progress += ['Java','Python']
reviewer_1.rate_homework(student_1, 'Python', 1), reviewer_1.rate_homework(student_1, 'Java', 10)
reviewer_1.rate_homework(student_1, 'Java', 5), reviewer_1.rate_homework(student_1, 'Java', 6)
reviewer_1.rate_homework(student_2, 'Java', 2), reviewer_1.rate_homework(student_2, 'Java', 4)
reviewer_1.rate_homework(student_2, 'Python', 8),reviewer_1.rate_homework(student_2, 'Python', 7)
student_list.append(student_1), student_list.append(student_2)
print("student_1 data structure:", student_1.__dict__)
print("student_2 data structure:", student_2.__dict__)

# --------- LECTURER LIST
lecturer_1 = Lecturer('David', 'Clark')
lecturer_1.courses_attached += ['Python', 'Java']
lecturer_2 = Lecturer('Peter', 'White')
lecturer_2.courses_attached += ['Python', 'C++']
student_1.rate_lecturer(lecturer_1, 'Python', 8), student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 5), student_1.rate_lecturer(lecturer_1, 'Java', 6)
student_1.rate_lecturer(lecturer_2, 'Python', 9), student_1.rate_lecturer(lecturer_2, 'Python', 12)
lecturer_list.append(lecturer_1), lecturer_list.append(lecturer_2)
print("lecturer_1 data structure:", lecturer_1.__dict__)
print("lecturer_2 data structure:", lecturer_2.__dict__)

# ----- PRINT -------
print("\n-> STUDENT GRADE COUNT")
grades_count = show_average_student_grade(student_list, "Java")
for key, value in grades_count.items():
    print(key.name, key.surname, value)

print("\n-> LECTURER GRADE COUNT")
grades_count = show_average_lecturer_grade(lecturer_list, "Python")
for key, value in grades_count.items():
    print(key.name, key.surname, value)

print("\n-> PRINT STUDENT")
print(student_1)

print("\n-> PRINT LECTURER")
print(lecturer_1)

print("\n-> COMPARE STUDENT GRADES")
print(student_1 > student_2)
print(student_1 < student_2)
print("\n-> COMPARE LECTURER GRADES")
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)