from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

"""   1) Створення моделі даних: Створіть просту модель даних для системи управління студентами. Модель може містити 
таблиці для студентів, курсів та їх відношень. Кожен студент може бути зареєстрований на декілька курсів. Наприклад, 
створити 5 курсів, та розподілити рандомно 20 студентів.
     2) Виконання базових операцій: Напишіть програму, 
яка додає нового студента до бази даних та додає його до певного курсу. Переконайтеся, що ці зміни коректно 
відображаються у базі даних.
     3) Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про 
студентів, зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
     4) Оновлення та видалення 
даних: Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних. 
     5) Можна використовувати будь яку ORM на Ваш вібир"""

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

Base = declarative_base()
engine = create_engine("sqlite:///mybase.db", echo=False)
Session = sessionmaker(bind=engine)

# Проміжна таблиця для зв’язку
student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


# Модель студентів
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    courses = relationship("Course", secondary=student_course, back_populates="students")


# Модель курсів
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", secondary=student_course, back_populates="courses")


# Клас-менеджер для роботи з БД
class StudentCourseManager:
    def __init__(self):
        self.session = Session()

    def create_tables(self):
        Base.metadata.create_all(engine)

    def seed_data(self):
        # Створює 5 курсів і 20 студентів
        course_names = ['Math', 'Physics', 'Biology', 'History', 'Programming']
        courses = [Course(name=name) for name in course_names]
        self.session.add_all(courses)
        self.session.commit()

        for i in range(1, 21):
            student = Student(name=f"Student {i}", age=random.randint(18, 25))
            student.courses = random.sample(courses, k=random.randint(1, 3))
            self.session.add(student)

        self.session.commit()

    def add_student(self, name, age, course_name):
        course = self.session.query(Course).filter_by(name=course_name).first()
        if course:
            student = Student(name=name, age=age)
            student.courses.append(course)
            self.session.add(student)
            self.session.commit()
            print(f"Додано студента {name} до курсу {course_name}")
        else:
            print(f"Курс {course_name} не знайдено.")

    def get_students_on_course(self, course_name):
        course = self.session.query(Course).filter_by(name=course_name).first()
        if course:
            print(f"Студенти на курсі {course.name}:")
            for s in course.students:
                print(f"{s.name} (вік: {s.age})")
        else:
            print(f"Курс {course_name} не знайдено.")

    def get_courses_for_student(self, student_name):
        student = self.session.query(Student).filter_by(name=student_name).first()
        if student:
            print(f"Курси для {student.name}:")
            for c in student.courses:
                print(c.name)
        else:
            print(f"Студент {student_name} не знайдений.")

    def update_student_name(self, old_name, new_name):
        student = self.session.query(Student).filter_by(name=old_name).first()
        if student:
            student.name = new_name
            self.session.commit()
            print(f"Ім’я змінено з {old_name} на {new_name}")
        else:
            print("Студента не знайдено.")

    def delete_student(self, name):
        student = self.session.query(Student).filter_by(name=name).first()
        if student:
            self.session.delete(student)
            self.session.commit()
            print(f"Студент {name} видалений.")
        else:
            print("Студента не знайдено.")


if __name__ == "__main__":
    manager = StudentCourseManager()

    # Створення таблиць і базових даних
    manager.create_tables()
    manager.seed_data()

    # Операції
    manager.add_student("Tetiana Lypnyk", 30, "Math")
    manager.get_courses_for_student("Tetiana Lypnyk")
    manager.get_students_on_course("Math")

    manager.update_student_name("Tetiana Lypnyk", "Tetiana Savchenko")
    manager.delete_student("Tetiana Savchenko")
