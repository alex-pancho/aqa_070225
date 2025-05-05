from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

Base = declarative_base()
engine = create_engine("sqlite:///students.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    students = relationship("Student", secondary=student_course, back_populates="courses")

Base.metadata.create_all(engine)

def create_courses():
    course_names = ["Math", "History", "Biology", "IT", "Physics"]
    for name in course_names:
        if not session.query(Course).filter_by(name=name).first():
            session.add(Course(name=name))
    session.commit()

# Create 20 students and randomly assign them to 1–3 courses
def create_students():
    if not session.query(Course).all():
        create_courses()
    courses = session.query(Course).all()
    for i in range(1, 21):
        name = f"Student {i}"
        if not session.query(Student).filter_by(name=name).first():
            student = Student(name=name)
            student.courses = random.sample(courses, k=random.randint(1, 3))
            session.add(student)
    session.commit()

# Add a new student and assign them to given courses
def add_student(name, course_names):
    existing = session.query(Student).filter_by(name=name).first()
    if existing:
        print(f"Student {name} already exists.")
        return
    courses = session.query(Course).filter(Course.name.in_(course_names)).all()
    student = Student(name=name, courses=courses)
    session.add(student)
    session.commit()

def get_students_by_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    return [s.name for s in course.students] if course else []

def get_courses_by_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    return [c.name for c in student.courses] if student else []

def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()

def update_course_name(old_name, new_name):
    course = session.query(Course).filter_by(name=old_name).first()
    if course:
        course.name = new_name
        session.commit()

def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()

def delete_course(name):
    course = session.query(Course).filter_by(name=name).first()
    if course:
        if course.students:
            print(f"Cannot delete course {name}, it has enrolled students.")
            return
        session.delete(course)
        session.commit()

if __name__ == "__main__":
    create_courses()
    create_students()

    add_student("Ivan", ["Math", "IT"])
    print("Students in course 'Math':", get_students_by_course("Math"))
    print("Courses for 'Student 1':", get_courses_by_student("Student 1"))

    update_student_name("Student 1", "Updated Student")
    update_course_name("Math", "Advanced Math")

    delete_student("Student 2")
    delete_course("Physics") 

    print("Finished. Data updated.")