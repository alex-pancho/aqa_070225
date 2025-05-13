"""
1.Створення моделі даних: Створіть просту модель даних для системи управління студентами. 
Модель може містити таблиці для студентів, курсів та їх відношень. 
Кожен студент може бути зареєстрований на декілька курсів. Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.
2.Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу. 
Переконайтеся, що ці зміни коректно відображаються у базі даних.
3.Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, 
зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
4.Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.
Можна використовувати будь яку ORM на Ваш вібир
"""

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

# Base class for all ORM models
Base = declarative_base()

# Creating a connection to the SQLite database
engine = create_engine("sqlite:///mybase3.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Many-to-many association table between students and courses
student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

# Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)

    # Many-to-many relationship to Course
    courses = relationship("Course", secondary=student_course, back_populates="students")

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age}, email='{self.email}')>"

# Course model
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    # Many-to-many relationship to Student
    students = relationship("Student", secondary=student_course, back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}')>"

# Create all database tables
Base.metadata.create_all(engine)

# Seed the database with initial test data
def seed_data():
    course_names = ["Data Science", "Cybersecurity", "Art History", "AI Basics", "Web Dev"]
    courses = [Course(title=name) for name in course_names]
    session.add_all(courses)
    session.commit()

    for i in range(1, 21):
        name = f"Student{i}"
        age = random.randint(13, 25)
        email = f"student{i}@example.com"

        if age < 15:
            print(f"Student {name} is too young ({age}) – not added.")
            continue

        student = Student(name=name, age=age, email=email)
        student.courses = random.sample(courses, k=random.randint(1, 3))
        session.add(student)

    session.commit()
    print("Seed data completed.")

# Add a new student with email and age validation
def add_student(name, age, email, course_title):
    if age < 15:
        print("Student too young to register.")
        return

    if "@" not in email:
        print("Invalid email format. '@' symbol is missing.")
        return

    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print("Course not found.")
        return

    student = Student(name=name, age=age, email=email)
    student.courses.append(course)
    session.add(student)
    session.commit()
    print(f"Student {name} added to {course_title}.")

# List all students enrolled in a given course
def get_students_by_course(title):
    course = session.query(Course).filter_by(title=title).first()
    if course:
        print(f"Students in course '{title}':")
        for student in course.students:
            print(f"  - {student.name}, {student.age} y.o., email: {student.email}")
    else:
        print("Course not found.")

# List all courses a student is enrolled in
def get_courses_by_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        print(f"{student.name} is enrolled in:")
        for course in student.courses:
            print(f"  - {course.title}")
    else:
        print("Student not found.")

# Update a student's name by their ID
def update_student_name(student_id, new_name):
    student = session.get(Student, student_id)
    if student:
        old_name = student.name
        student.name = new_name
        session.commit()
        print(f"Name changed from {old_name} to {new_name}.")
    else:
        print("Student not found.")

# Delete a student by their ID
def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Student {student.name} was deleted.")
    else:
        print("Student not found.")

# Main program logic
if __name__ == "__main__":
    seed_data()

    add_student("Katka", 22, "katka@example.com", "AI Basics")
    get_students_by_course("AI Basics")
    get_courses_by_student("Katka")

    update_student_name(1, "Katarina")
    delete_student(2)
