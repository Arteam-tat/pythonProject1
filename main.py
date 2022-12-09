class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lr(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course \
            in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avarage_rating(self):
        avarage = round(sum(sum(self.grades.values(), []))/len(sum(self.grades.values(), [])), 2)
        return avarage

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.avarage_rating()}\n\
Курсы в процессе изучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(self, Student):
            print('Not pair')
            return
        return self.avarage_rating() < other.avarage_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avarage_rating(self):
        average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 2)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.avarage_rating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.avarage_rating() < other.avarage_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


#Студенты
student_1 = Student('Ozzy', 'Osbourne', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в програмирование']
student_2 = Student('Charles', 'Manson', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['JS']
student_2.finished_courses += ['Введение в програмирование']

#Лекторы
lecturer_1 = Lecturer('Pablo', 'Eskobar')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Popugai', 'Kesha')
lecturer_2.courses_attached += ['Git']

#Ревьюверы
reviewer_1 = Reviewer('Travis', 'Scott')
reviewer_1.courses_attached += ['Git']
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Till', 'Lindemann')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['Python']

#rate_lr, rate_hw
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_1.rate_hw(student_2, 'Python', 2)
reviewer_2.rate_hw(student_1, 'Python', 1)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Git', 4)
reviewer_2.rate_hw(student_1, 'Git', 2)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_1.rate_hw(student_2, 'Python', 2)
reviewer_2.rate_hw(student_1, 'Python', 1)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Git', 4)
reviewer_2.rate_hw(student_1, 'Git', 2)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_2, 'Git', 9)

student_1.rate_lr(lecturer_1,'Python', 10)
student_1.rate_lr(lecturer_2, 'Git', 9)
student_2.rate_lr(lecturer_1, 'Python', 10)
student_2.rate_lr(lecturer_2, 'Git', 5)
student_1.rate_lr(lecturer_1, 'Python', 8)
student_1.rate_lr(lecturer_2, 'Git', 9)
student_2.rate_lr(lecturer_1, 'Python', 9)
student_2.rate_lr(lecturer_2, 'Git', 10)

all_student = [student_1, student_2]
all_lecturer = [lecturer_1, lecturer_2]


def av_grade_st(course, list=all_student):
    su = 0
    length = 0
    for st in list:
        if course in st.grades:
            su += sum(st.grades[course])
            length += len(st.grades[course])
    return f'Средний балл студентов за курс {course}: {round(su / length, 2)}'


def av_grade_lec(course, list=all_lecturer):
    su = 0
    length = 0
    for lec in list:
        if course in lec.grades:
            su += sum(lec.grades[course])
            length += len(lec.grades[course])
    return f'Средний балл лекторов за курс {course}: {round(su / length, 2)}'

print(reviewer_1)

print(reviewer_2)

print(student_1)

print(student_2)

print(student_1 < student_2)
print(lecturer_1 < lecturer_2)

print(av_grade_st('Python'))

print(av_grade_lec('Python'))
