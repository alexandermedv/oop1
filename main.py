
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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

lect = Lecturer('Some', 'Lector')
lect.courses_attached += ['Python']

best_student.rate_hw(lect, 'Python', 10)

print(best_student.grades)
print(lect.grades)
print(cool_mentor)