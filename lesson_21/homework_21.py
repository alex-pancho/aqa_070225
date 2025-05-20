"""
1) Створення моделі даних: Створіть просту модель даних для системи управління студентами. Модель може містити таблиці
для студентів, курсів та їх відношень. Кожен студент може бути зареєстрований на декілька курсів.
Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.
2) Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до
певного курсу. Переконайтеся, що ці зміни коректно відображаються у базі даних.
3) Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих
на певний курс, або курси, на які зареєстрований певний студент.
4) Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, а також видалення
студентів з бази даних.
5) Можна використовувати будь-яку ORM на Ваш вибір
"""

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import random

Base = declarative_base()


# Увімкнення зовнішніх ключів у SQLite
@event.listens_for(Engine, "connect")
def enforce_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    courses = relationship(
        "Course", secondary="student_courses", back_populates="students"
    )


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship(
        "Student", secondary="student_courses", back_populates="courses"
    )


class StudentCourses(Base):
    __tablename__ = "student_courses"
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)


def create_engine_and_session(db_url="sqlite:///mybase.db"):
    engine = create_engine(db_url, echo=True, connect_args={"check_same_thread": False})
    Session = sessionmaker(bind=engine)
    return engine, Session()


def seed_data(session):
    if session.query(Course).count() > 0 or session.query(Student).count() > 0:
        print("Дані вже існують.")
        return

    courses = [Course(name=f"Course {i}") for i in range(1, 6)]
    session.add_all(courses)
    session.commit()

    for i in range(20):
        student = Student(name=f"Student {i+1}", age=random.randint(18, 50))
        student.courses = random.sample(courses, random.randint(1, 3))
        session.add(student)
    session.commit()


def get_students_by_course(course_name, session):
    course = session.query(Course).filter_by(name=course_name).first()
    return course.students if course else []


def get_courses_by_student(student_name, session):
    student = session.query(Student).filter_by(name=student_name).first()
    return student.courses if student else []


def update_student(student_id, new_name, session):
    try:
        student = session.query(Student).filter_by(id=student_id).first()
        if student:
            student.name = new_name
            session.commit()
        else:
            print("Студента не знайдено.")
    except Exception as e:
        session.rollback()
        print(f"Помилка оновлення: {e}")


def delete_student(student_id, session):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        try:
            session.delete(student)
            session.commit()
            print("Студента видалено.")
        except Exception as e:
            session.rollback()
            print(f"Видалення заборонене: {e}")
    else:
        print("Студента не знайдено.")


def print_all_students(session):
    students = session.query(Student).all()
    print("Студенти:")
    for student in students:
        print(f"ID: {student.id}, Ім'я: {student.name}, Вік: {student.age}")


def print_all_courses(session):
    courses = session.query(Course).all()
    print("Курси:")
    for course in courses:
        print(f"ID: {course.id}, Назва: {course.name}")


def print_student_details(student_name, session):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        print(f"Студент:\nID: {student.id}, Ім'я: {student.name}, Вік: {student.age}")
        print("Відвідує курси:")
        for course in student.courses:
            print(f"- {course.name}")
    else:
        print("Студента не знайдено.")


def print_course_details(course_name, session):
    course = session.query(Course).filter_by(name=course_name).first()
    if course:
        print(f"Курс:\nID: {course.id}, Назва: {course.name}")
        print("Відвідують студенти:")
        for student in course.students:
            print(f"- {student.name}")
    else:
        print("Курс не знайдено.")


if __name__ == "__main__":
    engine, session = create_engine_and_session()
    Base.metadata.create_all(engine)
    seed_data(session)

    print_all_students(session)
    print_all_courses(session)
    print_student_details("Student 1", session)
    print_course_details("Course 1", session)

    update_student(1, "Updated Student 1", session)
    print_student_details("Updated Student 1", session)

    delete_student(1, session)
    print_all_students(session)
