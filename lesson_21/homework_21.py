from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

Base = declarative_base()
engine = create_engine("sqlite:///students.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Таблиця для зв’язку "багато до багатьох"
student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=student_course, back_populates="students")

    def __repr__(self):
        return f"<Student(name={self.name})>"

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary=student_course, back_populates="courses")

    def __repr__(self):
        return f"<Course(title={self.title})>"

Base.metadata.create_all(engine)

# 📌 Додаємо стартові курси і студентів
def seed_data():
    course_titles = ["Math", "History", "Biology", "Physics", "Art"]
    courses = [Course(title=title) for title in course_titles]
    session.add_all(courses)

    student_names = [f"Student{i}" for i in range(1, 21)]
    students = [Student(name=name) for name in student_names]

    for student in students:
        student.courses = random.sample(courses, random.randint(1, 3))
        session.add(student)

    session.commit()
    print("Дані успішно додано!")

# ➕ Додаємо нового студента і записуємо його на курс
def add_student_to_course(student_name, course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print("Курс не знайдено 😢")
        return
    student = Student(name=student_name)
    student.courses.append(course)
    session.add(student)
    session.commit()
    print(f"{student_name} доданий на курс {course_title}!")

# 🔍 Виводимо студентів, які записані на курс
def get_students_by_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        print(f"Студенти на курсі {course_title}:")
        for s in course.students:
            print(f"- {s.name}")
    else:
        print("Курс не знайдено")

# 🔍 Виводимо курси, на які записаний студент
def get_courses_by_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        print(f"{student.name} записаний на курси:")
        for c in student.courses:
            print(f"- {c.title}")
    else:
        print("Студента не знайдено")

# ✏️ Оновлення імені студента
def update_student_name(student_id, new_name):
    student = session.query(Student).get(student_id)
    if student:
        old_name = student.name
        student.name = new_name
        session.commit()
        print(f"{old_name} тепер {new_name}")
    else:
        print("Студент не знайдений")

# ❌ Видалення студента
def delete_student(student_id):
    student = session.query(Student).get(student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Студент {student.name} видалений.")
    else:
        print("Студент не знайдений")

# 🧪 Прості тести
if __name__ == "__main__":
    # seed_data()  # Розкоментуй один раз для генерації даних
    add_student_to_course("Katya", "Art")
    get_students_by_course("Art")
    get_courses_by_student("Katya")
    update_student_name(1, "Andriy")
    delete_student(2)