class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def add_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] += [grade]
        else:
            self.grades[course] = [grade]

    def average_rating(self):
        total_sum = sum(sum(grade_list) for grade_list in self.grades.values())
        total_count = sum(len(grade_list) for grade_list in self.grades.values()) or 0
        return round(total_sum / total_count, 1) if total_count > 0 else 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'

    def rate_lecture(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer) and self.is_course_attached(course) and \
              course in lecturer.courses_attached:
                lecturer.add_grade(course, grade)
            else:
                print("Ошибка")

    def __lt__(self, other):
      if not isinstance(other, Lecturer):
        raise TypeError("Можно сравнивать только объекты типа Lecturer")
      return self.average_rating() < other.average_rating()


    def __gt__(self, other):
      if not isinstance(other, Lecturer):
        raise TypeError("Можно сравнивать только объекты типа Lecturer")
      return self.average_rating() > other.average_rating()

    def __eq__(self, other):
      if not isinstance(other, Lecturer):
        raise TypeError("Можно сравнивать только объекты типа Lecturer")
      return self.average_rating() == other.average_rating()

def average_lecture_grade_for_course(lecturers, course):
  grades = []
  for lecturer in lecturers:
    if course in lecturer.grades:
      grades.extend(lecturer.grades[course])
    return round(sum(grades) / len(grades), 1) if grades else 0

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def is_course_attached(self, course):
        return course in self.courses_in_progress

    def add_finished_course(self, course_name):
      self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and self.is_course_attached(course) and \
           course in lecturer.courses_attached:
            lecturer.add_grade(course, grade)
        else:
            print("Ошибка")

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def is_course_attached(self, course):
        return course in self.courses_in_progress

    def average_grades(self):
        total_sum = sum(sum(grade_list) for grade_list in self.grades.values())
        total_count = sum(len(grade_list) for grade_list in self.grades.values()) or 0
        return round(total_sum / total_count, 1) if total_count > 0 else 0.

    def __lt__(self, other):
      if not isinstance(other, Student):
        raise TypeError("Можно сравнивать только объекты типа Student")
      return self.average_grades() < other.average_grades()

    def __gt__(self, other):
      if not isinstance(other, Student):
        raise TypeError("Можно сравнивать только объекты типа Student")
      return self.average_grades() > other.average_grades()

    def __eq__(self, other):
      if not isinstance(other, Student):
        raise TypeError("Можно сравнивать только объекты типа Student")
      return self.average_grades() == other.average_grades()

    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

def average_hw_grade_for_course(students, course):
  grades = []
  for student in students:
    if course in student.grades:
      grades.extend(student.grades[course])
    return round(sum(grades) / len(grades), 1) if grades else 0



reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('William ', 'Brandywine')

lecturer1 = Lecturer('Derek ', 'Knight')
lecturer2 = Lecturer('Johnny ', 'Worthington ')

student1 = Student('Ruoy', 'Eman', 'male')
student2 = Student('Michael ', 'Wazowski', 'male')

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

student1.add_courses('Git')
student1.add_courses('Python')
student2.add_courses('Python')
student2.add_courses('Java')

student1.add_finished_course('Java')
student2.add_finished_course('Git')

reviewer1.courses_attached.append('Python')
reviewer1.courses_attached.append('Java')
reviewer2.courses_attached.append('Python')
reviewer2.courses_attached.append('Git')

lecturer1.courses_attached.append('Python')
lecturer1.courses_attached.append('Java')
lecturer2.courses_attached.append('Python')
lecturer2.courses_attached.append('Git')


reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 9)


student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer1, 'Python', 6)
student2.rate_lecture(lecturer2, 'Python', 7)


average_student_grade = average_hw_grade_for_course(students, 'Python')
average_lecturer_grade = average_lecture_grade_for_course(lecturers, 'Python')

print('\nИнформация о студентах:\n')
print(student1,'\n')
print(student2)

print('\nИнформация о проверяющих:\n')
print(reviewer1,'\n')
print(reviewer2)

print('\nИнформация о лекторах:\n')
print(lecturer1,'\n')
print(lecturer2)


print(f"\nСредняя оценка за домашние задания по курсу 'Python': {average_student_grade}")
print(f"Средняя оценка за лекции по курсу 'Python': {average_lecturer_grade}\n")


if lecturer1 < lecturer2:
    print(f'Средняя оценка {lecturer1.name} {lecturer1.surname} < средней оценки {lecturer2.name} {lecturer2.surname}')
elif lecturer1 > lecturer2:
    print(f'Средняя оценка {lecturer1.name} {lecturer1.surname} > средней оценки {lecturer2.name} {lecturer2.surname}')
else:
    print(f'Средняя оценка {lecturer1.name} {lecturer1.surname} = средней оценке {lecturer2.name} {lecturer2.surname}')


if student1 < student2:
    print(f'Средняя оценка {student1.name} {student1.surname} < средней оценки {student2.name} {student2.surname}')
elif student1 > student2:
    print(f'Средняя оценка {student1.name} {student1.surname} > средней оценки {student2.name} {student2.surname}')
else:
    print(f'Средняя оценка {student1.name} {student1.surname} = средней оценке {student2.name} {student2.surname}')