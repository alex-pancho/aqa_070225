"""Створення моделі даних: Створіть просту модель даних для системи управління студентами. 
Модель може містити таблиці для студентів, курсів та їх відношень. 
Кожен студент може бути зареєстрований на декілька курсів. 
Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.
Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
 Переконайтеся, що ці зміни коректно відображаються у базі даних.
Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс,
 або курси, на які зареєстрований певний студент.
Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.
Можна використовувати будь яку ORM на Ваш вібир"""

import random
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

base = declarative_base()
engine = create_engine("sqlite:///mybase.db") 


"""Асоціативна таблиця використовується для реалізації зв’язку багато-до-багатьох (many-to-many)
Це окрема таблиця, яка зберігає зв’язки між двома іншими таблицями. 
Вона зазвичай містить два зовнішні ключі — по одному до кожної з пов’язаних таблиць.
base.metadata: Це мета-дані, що містять опис всіх таблиць, визначених у вашому SQLAlchemy ORM. 
Це дозволяє SQLAlchemy знати, де зберігати та як організовувати таблицю в базі даних.
Таблиця student_course не має власного автозгенерованого стовпця з унікальним ідентифікатором, 
оскільки її роль — зберігати зв'язки між студентами та курсами. 
Кожна пара (student_id, course_id) є унікальною в цій таблиці
"""
student_course = Table(
    'student_course',
    base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('course.id'), primary_key=True)
)

class Students(base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String, unique=True)
    
    # many-to-many relationship
    courses = relationship("Course", secondary=student_course, back_populates="students")


class Course(base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String)
 
    #  many-to-many relationship
    students = relationship("Students", secondary=student_course, back_populates="courses")
    
       
base.metadata.create_all(engine)

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

# Додавання нового cтудента
def add_new_student(name, phone, session=session):
    try:
        new_student = Students(name=name, phone=phone)
        session.add(new_student)
        session.commit()
    except Exception as e:
        print(f'Error happens: {e}')
        session.rollback()

#Довавання студента до курсу
def assign_student_to_a_courses(phone, courses:list):
    if not isinstance(courses, list):
        raise ValueError (" courses should be a list")
    student = session.query(Students).filter_by(phone=phone).first()
    if not student:
        print("Student not found")
        return
    
    existing_courses = []
    all_courses = session.query(Course).all()
    for course in all_courses:
        existing_courses.append(course.name)

    for course in courses:
        if course in existing_courses:
            current_course = session.query(Course).filter_by(name=course).first()
            if current_course not in student.courses:
                
                student.courses.append(current_course)
            else:
                continue
        else:     
            print(f"Course {course} is not found.")
            continue
        
    session.commit()
          
        

#редагування студента
def edit_student(student_to_edit_phone, field, new_value, session=session):
    student = session.query(Students).filter_by(phone=student_to_edit_phone).first()
    if not student:
        print("Student not found")
        return
    if hasattr(student, field):
        setattr(student, field,  new_value)
        session.commit() 
    else:
        print(f"Student has not {field} field")
        return

# видалення студента
def delete(student_to_delete_phone, session=session):
    student = session.query(Students).filter_by(phone=student_to_delete_phone).first()
    if not student:
        print("Student not found")
        return
    session.delete(student)
    session.commit() 

#додавання курсу
def add_new_item_to_course(name, session=session):
    courses = session.query(Course).filter_by(name = name).all()
    if courses:
        print(f"Course {name} already exist")
        return
    new_cource = Course(name=name)
    session.add(new_cource)
    session.commit()

#вибірка студентів за курсом
def select_students_by_course(course_name_to_filter_by, session=session):
    course = session.query(Course).filter_by(name = course_name_to_filter_by).first()
    if not course:
        print("Course not found")
        return
    students_by_course = []
    for student in course.students:
        student_name = student.name
        students_by_course.append(student_name)
    return students_by_course


#вибірка курсів заданого студента
def select_courses_by_student(student_phone, session=session):
    student = session.query(Students).filter_by(phone=student_phone).first()
    if not student:
        print("Student not found")
    
    courses_list = []
    for course in student.courses:
        course_name = course.name
        courses_list.append(course_name)
    return courses_list

#вибірка всіх студентів
def select_all_students():
    all_students = session.query(Students).all()
    for student in all_students:
        course_list =[]
        for course in student.courses:
            course_list.append(course.name)
        print(f"{ student.id},   { student.name},   { student.phone}, Courses:  { course_list}")
    return all_students

#вибірка курсів
def select_all_courses():
    all_courses = session.query(Course).all()
    for course in all_courses:
        print(f"{course.id}, {course.name}")
    return all_courses


if __name__ == "__main__":
    
    students = [
    ("Andrew", "+380501112233"),
    ("Olga", "+380502223344"),
    ("Vitalii", "+380503334455"),
    ("Iryna", "+380504445566"),
    ("Dmytro", "+380505556677"),
    ("Mariya", "+380506667788"),
    ("Artem", "+380507778899"),
    ("Kateryna", "+380508889900"),
    ("Serhii", "+380509990011"),
    ("Anastasia", "+380931112233"),
    ("Yevhen", "+380932223344"),
    ("Tetiana", "+380933334455"),
    ("Mykola", "+380934445566"),
    ("Svitlana", "+380935556677"),
    ("Vladyslav", "+380936667788"),
    ("Lilia", "+380937778899"),
    ("Taras", "+380938889900"),
    ("Olena", "+380939990011"),
    ("Yulia", "+380991112233"),
    ("Viktor", "+380992223344")
]
   # for student in students:
   #     add_new_student(student[0], student[1])
    add_new_item_to_course ("biology")
    courses = ["math", "art", "stem", "music", "biology"]
    #for student in students:
    #    random_course = [(random.choice(courses))]
    #   assign_student_to_a_courses(student[1], random_course)
    
    #select_all_courses()
    edit_student("+380992223344", "phone", "+380999999999")
    delete("0995124549")
    select_all_students()
    print(select_students_by_course("math"))
    print(select_courses_by_student("+380939990011"))
