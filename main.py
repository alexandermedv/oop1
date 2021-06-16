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

        if kol > 0:
            sred = summa / kol
        else:
            sred = 0

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

    def compare(self, other_student):
        """Сравнение лекторов по оценкам студентов"""

        summa1 = 0
        kol1 = 0
        for key in self.grades:
            summa1 += sum(self.grades[key])
            kol1 += len(self.grades[key])

        if kol1 > 0:
            sred1 = summa1 / kol1
        else:
            sred1 = 0

        summa2 = 0
        kol2 = 0

        for key in other_student.grades:
            summa2 += sum(other_student.grades[key])
            kol2 += len(other_student.grades[key])
        if kol2 > 0:
            sred2 = summa2 / kol2
        else:
            sred2 = 0

        if sred1 > sred2:
            return self
        else:
            return other_student


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

        if kol > 0:
            sred = summa/kol
        else:
            sred = 0

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


# Создаем по 2 экземпляра каждого класса
first_student = Student('Alexander', 'Medvedev', 'Male')
second_student = Student('Valentina', 'Medvedeva', 'Female')
first_reviewer = Reviewer('Alexander', 'Bardin')
second_reviewer = Reviewer('Sergey', 'Rozhnev')
first_lector = Lecturer('Oleg', 'Bulygin')
second_lector = Lecturer('Andrey', 'Aseev')

# Используем все методы классов
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Java']
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Java']
first_lector.courses_attached += ['Python']
second_lector.courses_attached += ['Java']
first_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Java']
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Java', 2)
first_student.rate_hw(first_lector, 'Python', 10)
first_student.rate_hw(first_lector, 'Python', 8)
second_student.rate_hw(second_lector, 'Java', 8)
second_student.rate_hw(second_lector, 'Java', 6)

# Выводим информацию о каждом экземпляре
print('Информация о первом студенте:\n', first_student, sep='')
print('Информация о втором студенте:\n', second_student, sep='')
print('Информация о первом проверяющем:\n', first_reviewer, sep='')
print('Информация о втором проверяющем:\n', second_reviewer, sep='')
print('Информация о первом лекторе:\n', first_lector, sep='')
print('Информация о втором лекторе:\n', second_lector, sep='')
print('Выше оценки у лектора:\n', first_lector.compare(second_lector), sep='')
print('Выше оценки у студента:\n', first_student.compare(second_student), sep='')
