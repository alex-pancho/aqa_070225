from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

base = declarative_base()
engine = create_engine("sqlite:///mybase.db", echo=True) 

student_course_association = Table(
    'student_course_association',
    base.metadata, 
    Column('student_id', Integer, ForeignKey('students.student_id')),
    Column('course_id', Integer, ForeignKey('courses.course_id'))
    
)

class Student(base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    grad_year = Column(Integer)
    courses = relationship("Courses", secondary=student_course_association, back_populates="students")


    
class Courses(base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String)
    # Встановлення відношення "один до багатьох" з таблицею Employee
    students = relationship("Student", secondary=student_course_association, back_populates="courses")
    


base.metadata.create_all(engine)

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

def add_new_item_to_courses(course_name='Mathimatics', session=session):
    new_course = Courses(course_name=course_name)
    session.add(new_course)
    session.commit()

# Додавання нового користувача
def add_new_item_to_students(name='Andrey', last_name='Shevchenko', grad_year = 2025, course_names = None, session=session):
    new_student = Student(name=name, last_name=last_name, grad_year=grad_year)
    if course_names is None:
        course_names = []

    for cname in course_names:
        new_course =  session.query(Courses).filter_by(course_name = cname).first()
        if new_course:
            new_student.courses.append(new_course)
            
        
    session.add(new_student)
    session.commit()



def select_all_students():
    all_students = session.query(Student).all()
    return all_students

def select_all_courses():
    all_courses = session.query(Courses).all()
    return all_courses

def get_courses_for_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        print(f"{student.name} записан на курси:")
        for course in student.courses:
            print(f"- {course.course_name}")
    else:
        print("Студент не знайдений.")

def get_students_by_course(course_name):
    course = session.query(Courses).filter_by(course_name=course_name).first()
    if course:
        print(f"Студенти на курсі {course_name}:")
        for student in course.students:
            print(f"- {student.name} {student.last_name}")

def update_student_name(student_id, new_name):
    student = session.query(Student).get(student_id)
    if student:
        student.name = new_name
        session.commit()

def delete_student(student_id):
    student = session.query(Student).get(student_id)
    if student:
        session.delete(student)
        session.commit()
        
if __name__ == "__main__":
    
    add_new_item_to_courses(course_name='Physics')
    add_new_item_to_courses(course_name='Chemistry')
    add_new_item_to_courses(course_name='Computer science')
    add_new_item_to_courses(course_name='Bio')
    
    add_new_item_to_students(name='Anna', last_name='Shevchenko', grad_year = 2025, course_names=["Physics"])
    add_new_item_to_students(name='Andrey', last_name='Shevchenko', grad_year = 2025, course_names=["Computer science", 'Bio', 'Physics'])
    add_new_item_to_students(name='Mariia', last_name='Shevchenko', grad_year = 2025, course_names= ['Chemistry'])
    # add_new_item_to_students(name='Anna', last_name='Shevchenko', grad_year = 2025, course_id = 4)
    # add_new_item_to_students(name='Daniil', last_name='Shevchenko', grad_year = 2025, course_id = 3)
    # add_new_item_to_students(name='Pavlo', last_name='Shevchenko', grad_year = 2025, course_id = 5)
    # add_new_item_to_students(name='Iryna', last_name='Shevchenko', grad_year = 2025, course_id = 2)
    # add_new_item_to_students(name='Olga', last_name='Shevchenko', grad_year = 2025, course_id = 1)
    # add_new_item_to_students(name='Andrii', last_name='Shevchenko', grad_year = 2025, course_id = 1)
    print("\n--- ВСІ СТУДЕНТИ ---")
    for student in select_all_students():
        print(f"{student.student_id}: {student.name} {student.last_name}, {student.grad_year}")

    print("\n--- ВСІ КУРСИ ---")
    for course in select_all_courses():
        print(f"{course.course_id}: {course.course_name}")

    print("\n--- КУРСИ АННИ ---")
    get_courses_for_student("Anna")

    print("\n--- СТУДЕНТИ НА ФІЗИЦІ ---")
    get_students_by_course('Physics')

    print("\n--- ОНОВЛЕННЯ ІМʼЯ ---")
    update_student_name(1, "Ann")

    print("\n--- ВИДАЛЕННЯ СТУДЕНТА ---")
    delete_student(2)

    print("\n--- ПІСЛЯ ВИДАЛЕННЯ ---")
    for student in select_all_students():
        print(f"{student.student_id}: {student.name} {student.last_name}, {student.grad_year}")


   

