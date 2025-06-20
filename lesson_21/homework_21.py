from sqlalchemy import create_engine, Column, Integer ,String ,Table, ForeignKey 
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random
from faker import Faker

Base = declarative_base()

student_course = Table('student_course', Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ ='students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship('Course', secondary=student_course, back_populates='students')

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name})>"

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    students = relationship('Student', secondary=student_course, back_populates='courses')

    def __repr__(self):
        return f"<Course(id={self.id}, title={self.title})>"

engine = create_engine('sqlite:///students_courses.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

course_titles = ['Математика', 'Фізика', 'Інформатика', 'Історія', 'Хімія']
courses = [Course(title=title) for title in course_titles]
session.add_all(courses)
session.commit()

fake = Faker('uk_UA')

students = [Student(name=fake.name()) for _ in range(20)]
session.add_all(students)
session.commit()

for student in students:
    selected_courses = random.sample(courses, k=random.randint(1, 3))
    student.courses.extend(selected_courses)

session.commit()

print("Студенти та їхні курси після розподілу:")
for student in students:
    print(f"{student.name} навчається на курсах: {[c.title for c in student.courses]}")

def add_student(name, course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print(f"Курс '{course_title}' не знайдено")
        return

    new_student = Student(name=name)
    new_student.courses.append(course)
    session.add(new_student)
    session.commit()
    print(f"Додано студента {name} на курс {course_title}")

add_student(fake.name(), 'Інформатика')

def get_students_on_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print(f"Курс '{course_title}' не знайдено")
        return []
    return course.students

print("\nСтуденти на курсі 'Інформатика':")
for student in get_students_on_course('Інформатика'):
    print(student.name)

def get_courses_for_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if not student:
        print(f"Студента '{student_name}' не знайдено")
        return []
    return student.courses

def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if not student:
        print(f"Студента '{old_name}' не знайдено")
        return
    student.name = new_name
    session.commit()
    print(f"Ім’я студента оновлено з {old_name} на {new_name}")

def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if not student:
        print(f"Студента '{name}' не знайдено")
        return
    session.delete(student)
    session.commit()
    print(f"Студента {name} видалено")