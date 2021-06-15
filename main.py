class Student:
    """Класс Студент"""
    def __init__(self, name, surname, gender):
        """Инициализация класса"""
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        """Вывод информации класса"""

        summa = 0
        kol = 0

        for key in self.grades:
            summa += sum(self.grades[key])
            kol += len(self.grades[key])

        sred = summa / kol

        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + \
               '\n' + 'Средняя оценка за домашние задания: ' + str(round(sred, 1)) + \
               '\n' + 'Курсы в процессе изучения: ' + ', '.join(self.courses_in_progress) + \
               '\n' + 'Завершенные курсы: ' + ', '.join(self.finished_courses)

    def rate_hw(self, lecturer, course, grade):
        """Выставление оценок лектору"""
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    """Класс преподавателей"""
    def __init__(self, name, surname):
        """Инициализация класса"""
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс лекторов. Наследуется из класса преподавателей."""

    def __init__(self, name, surname):
        """Инициализация класса"""
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        """Вывод информации класса"""

        summa = 0
        kol = 0

        for key in self.grades:
            summa += sum(self.grades[key])
            kol += len(self.grades[key])

        sred = summa/kol

        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + \
               '\n' + 'Средняя оценка за лекции: ' + str(round(sred, 1))

    def compare(self, other_lector):
        """Сравнение лекторов по оценкам студентов"""

        summa1 = 0
        kol1 = 0
        for key in self.grades:
            summa1 += sum(self.grades[key])
            kol1 += len(self.grades[key])
        sred1 = summa1 / kol1

        summa2 = 0
        kol2 = 0

        for key in other_lector.grades:
            summa2 += sum(other_lector.grades[key])
            kol2 += len(other_lector.grades[key])

        sred2 = summa2 / kol2

        if sred1 > sred2:
            return self
        else:
            return other_lector


class Reviewer(Mentor):
    """Класс проверяющих. Наследуется из класса преподавателей."""

    def rate_hw(self, student, course, grade):
        """Выставление оценок студенту"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Вывод информации класса"""

        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname


def student_grades(student_list, course):
    """Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса"""

    summa = 0
    kol = 0
    for student in student_list:
        summa += sum(student.grades[course])
        kol += len(student.grades[course])
    sred = summa / kol

    return str(round(sred, 1))


def lector_grades(lector_list, course):
    """Подсчет средней оценки за лекции всех лекторов в рамках конкретного курса"""

    summa = 0
    kol = 0
    for lector in lector_list:
        summa += sum(lector.grades[course])
        kol += len(lector.grades[course])
    sred = summa / kol

    return str(round(sred, 1))


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 2)

lect = Lecturer('Some', 'Lector')
lect.courses_attached += ['Python']

best_student.rate_hw(lect, 'Python', 10)
best_student.rate_hw(lect, 'Python', 10)
best_student.rate_hw(lect, 'Python', 5)

second_lector = Lecturer('Other', 'Lector')
second_lector.courses_attached += ['Java']

best_student.courses_in_progress += ['Java']
best_student.rate_hw(second_lector, 'Java', 9)
best_student.rate_hw(second_lector, 'Java', 9)
best_student.rate_hw(second_lector, 'Java', 9)

print(best_student.grades)
print(lect.grades)
print(cool_mentor)
print(lect)
print(best_student)
print(lect.compare(second_lector))
print(student_grades([best_student], 'Python'))
print(lector_grades([second_lector], 'Java'))
