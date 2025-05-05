# 1. Створення моделі даних: Створіть просту модель даних для системи управління студентами. 
# Модель може містити таблиці для студентів, курсів та їх відношень. Кожен студент може бути 
# зареєстрований на декілька курсів. Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.
# 2. Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу. 
# Переконайтеся, що ці зміни коректно відображаються у базі даних.
# 3. Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, 
# зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
# 4. Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, 
# а також видалення студентів з бази даних.
# 5. Можна використовувати будь яку ORM на Ваш вибір

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, func, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


base = declarative_base()
engine = create_engine("sqlite:///hwbase.db", echo=True) 

# Проміжна таблиця для зв’язку "багато до багатьох"
student_course = Table(
    'student_course',
    base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

class Student(base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    courses = relationship("Course", secondary=student_course, back_populates="students") # Встановлення зв’язку "багато до багатьох" з таблицею Course

class Course(base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    students = relationship("Student", secondary=student_course, back_populates="courses") # Встановлення зв’язку "багато до багатьох" з таблицею Student

base.metadata.create_all(engine)

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

def add_new_student(first_name, last_name, course_names, session=session):
    """
    Adds a new student to the database and registers them in one or more courses.
    The student will be added to the courses specified in the course_names list.
    """
    selected_courses = session.query(Course).filter(Course.course_name.in_(course_names)).all()
    if not selected_courses:
        print("No valid courses found.")
        return
    new_student = Student(first_name=first_name, last_name=last_name)
    new_student.courses.extend(selected_courses) #додаємо декілька курсів
    session.add(new_student)
    session.commit()

def get_all_students_on_course(course_name):
    """
    Prints a list of students registered in a given course.
    Displays the first and last name of each student in the specified course.
    """
    course = session.query(Course).filter_by(course_name=course_name).first()
    if not course:
        print(f"Course '{course_name}' not found!")
        return
    print(f"Students registered in course '{course.course_name}':")
    for student in course.students:
        print(f"- {student.first_name} {student.last_name}")

def get_courses_by_student(first_name, last_name, session=session):
    """
    Prints a list of courses a specific student is registered for.
    Displays the course names the student is enrolled in.
    """
    student = session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()
    if not student:
        print(f"Student '{first_name} {last_name}' not found.")
        return
    
    print(f"Courses registered by {student.first_name} {student.last_name}:")
    for course in student.courses:
        print(f"- {course.course_name}")

def update_student_name(old_first_name, old_last_name, new_first_name, new_last_name):
    """
    Updates the name of an existing student.
    The student's first name and last name will be updated to the new values.
    """
    student = session.query(Student).filter_by(first_name=old_first_name, last_name=old_last_name).first()
    if not student:
        print("Student not found.")
        return
    student.first_name = new_first_name
    student.last_name = new_last_name
    session.commit()

def update_course_name(old_course_name, new_course_name, session=session):
    """
    Updates the name of an existing course.
    The course's name will be changed to the new course name provided.
    """
    course = session.query(Course).filter_by(course_name=old_course_name).first()
    if not course:
        print(f"Course '{old_course_name}' not found.")
        return
    course.course_name = new_course_name
    session.commit()

def delete_student(first_name, last_name):
    """
    Deletes a student from the database.
    The student with the specified first and last name will be removed from the database.
    """
    student = session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()
    if not student:
        print("Student not found.")
        return
    session.delete(student)
    session.commit()

if __name__ == "__main__":
    # Task 1
    # Створення курсів
    it_course = Course(course_name='IT')
    hr_course = Course(course_name='HR')
    finance_course = Course(course_name='Finance')
    marketing_course = Course(course_name='Marketing')
    logistics_course = Course(course_name='Logistics')

    courses = [it_course, hr_course, finance_course, marketing_course, logistics_course]

    session.add_all(courses)
    session.commit()

    # Створення студентів
    students = [
        Student(first_name='Andrew', last_name='Shevchenko'),
        Student(first_name='Olena', last_name='Kovalchuk'),
        Student(first_name='Ihor', last_name='Bondar'),
        Student(first_name='Maryna', last_name='Demchenko'),
        Student(first_name='Taras', last_name='Hnatyuk'),
        Student(first_name='Svitlana', last_name='Kuzmenko'),
        Student(first_name='Victor', last_name='Lytvyn'),
        Student(first_name='Natalia', last_name='Melnyk'),
        Student(first_name='Oleksandr', last_name='Solovey'),
        Student(first_name='Iryna', last_name='Tkachenko'),
        Student(first_name='Dmytro', last_name='Petrenko'),
        Student(first_name='Kateryna', last_name='Zhuk'),
        Student(first_name='Yurii', last_name='Oliinyk'),
        Student(first_name='Anastasiia', last_name='Romaniuk'),
        Student(first_name='Bohdan', last_name='Moroz'),
        Student(first_name='Valentyna', last_name='Syvorenko'),
        Student(first_name='Serhii', last_name='Havryliuk'),
        Student(first_name='Liudmyla', last_name='Tsymbaliuk'),
        Student(first_name='Roman', last_name='Yaremchuk'),
        Student(first_name='Oksana', last_name='Levchenko')
    ]

    # Призначення курсів циклом
    for i, student in enumerate(students):
        student.courses = [courses[i % len(courses)]]

    session.add_all(students)
    session.commit()

    # # Task 2
    # # Додавання нового студента до курсу
    # add_new_student("Julia", "Lazurkevych", ["IT", "HR", "Finance"], session)

    # Task 3
    # # отримання студентів за курсом
    # get_all_students_on_course('IT')
    # get_all_students_on_course('HR')
    # get_all_students_on_course('Finance')
    # # отримання курсів за студентом
    # get_courses_by_student("Julia", "Lazurkevych")

    # Task 4
    # # оновлення даних студента
    # update_student_name("Julia", "Lazurkevych", "Iuliia", "Lazurkevych")
    # # оновлення курсу
    # update_course_name("Finance", "Accounting")
    # # видалення студента
    # delete_student("Iuliia", "Lazurkevych")