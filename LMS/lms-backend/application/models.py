# database models/table definitions
from .database import *
import secrets

class StudentCourse(db.Model):
    __table_name__='student_course'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))
    def __init__(self, si, ci):
        self.student_id=si
        self.course_id=ci


class Student(db.Model):
    __tablename__='student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    API_token=db.Column(db.String(50), unique=True, nullable=False)
    current_courses = db.relationship(StudentCourse, uselist=True, backref='student')
    def __init__(self, sn, pwd, em):
        self.name = sn
        self.password = pwd
        self.email = em
        self.API_token=secrets.token_urlsafe(50)

class Course(db.Model):
    __tablename__='course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    short_desc = db.Column(db.String(None), nullable=False)
    desc = db.Column(db.String(None), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    instructor = db.Column(db.String(50), nullable=False)
    topics = db.Column(db.String(None), nullable=False)
    def __init__(self, cn, sd, de, du, pr, i, t):
        self.name = cn
        self.short_desc=sd
        self.desc=de
        self.duration=du
        self.price=pr
        self.instructor=i
        self.topics = t
        
class Question(db.Model):
    __tablename__='questions'
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))
    question = db.Column(db.String(500), nullable=False)
    quiz_type  = db.Column(db.String(25), nullable=False) #"assignment" or "prereq"
    question_type = db.Column(db.String(25), nullable=False)  #"MCQ" or "string" or "coding"
    option_a = db.Column(db.String(100), nullable=True)
    option_b = db.Column(db.String(100), nullable=True)
    option_c = db.Column(db.String(100), nullable=True)
    option_d = db.Column(db.String(100), nullable=True)
    answer_option = db.Column(db.String(100), nullable=True)
    answer = db.Column(db.String(500), nullable=True)
    def __init__(self, ci, q, qt, qut, oa=None, ob=None, oc=None, od=None, ao=None, a=None):
        self.question = q
        self.course_id = ci
        self.quiz_type = qt
        self.question_type=qut
        self.option_a=oa
        self.option_b=ob
        self.option_c=oc
        self.option_d=od
        self.answer=a
        self.answer_option=ao

db.create_all()
db.session.commit()