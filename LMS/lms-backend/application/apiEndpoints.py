import datetime
import bcrypt
from flask import *
from flask import current_app as app
from flask_restful import *
from .models import *
import requests
from jinja2 import Template
from application import tasks
from application import cacheable

api = Api(app)


class LoginAPI(Resource):
    def get(self):
        return 'ok', 200

    def post(self):
        try:
            try:
                json_values = request.json
            except:
                return{'status': 'error', 'message': 'no update parameters'}
            un = json_values.get('username', False)
            pwd = json_values.get('password', False)
            if not un:
                return{'status': 'error', 'message': 'username required'}
            if not pwd:
                return{'status': 'error', 'message': 'password required'}
            currentUser = Student.query.filter_by(name=un).first()
            if currentUser:
                if bcrypt.checkpw(bytes(pwd, 'utf_8'), currentUser.password):
                    return {'status': 'success', 'message': 'logged in', 'username': un, 'user_id': currentUser.user_id, 'access token': currentUser.API_token}
                else:
                    return{'status': 'error', 'message': 'wrong password'}

            else:
                return{'status': 'error', 'message': 'user not present'}
        except:
            abort(500)
class SignupAPI(Resource):
    def get(self):
        return 'ok', 200

    def post(self):
        try:
            try:
                json_values = request.json
            except:
                return{'status': 'error', 'message': 'no parameters'}
            un = json_values.get('username', False)
            pwd = json_values.get('password', False)
            em = json_values.get('email', False)
            if not un:
                return{'status': 'error', 'message': 'username required'}
            if not em:
                return{'status': 'error', 'message': 'email required'}
            if not pwd:
                return{'status': 'error', 'message': 'password required'}
            currentUser = Student.query.filter_by(name=un).first()
            if currentUser:
                return{'status': 'error', 'message': 'User already present'}
            slt = bcrypt.gensalt(5)
            pwd = bytes(pwd, 'utf_8')
            pwd = bcrypt.hashpw(pwd, slt)
            newUser = Student(un, pwd, em)
            db.session.add(newUser)
            db.session.commit()
            return{'status': 'success', 'message': 'successfully signed up', 'username': un, 'user_id': newUser.user_id, 'access token': newUser.API_token}
        except:
            abort(500)

class CourseAllResource(Resource):
    def get(self):  # get all courses available
        try:
            course_query = Course.query.all()
            courses = []
            for i in course_query:
                td = {
                    'id': i.course_id,
                    'name': i.name,
                    'short_desc': i.short_desc,
                    'desc': i.desc,
                    'duration': i.duration,
                    'price': i.price,
                    'instructor': i.instructor
                }
                courses.append(td)

            return {'status': 'success', 'data': courses}
        except:
            abort(500)

    def post(self):  # add a course into database
        try:
            # Extract data from request JSON
            data = request.get_json()
            name = data.get('name')
            short_desc = data.get('short_desc')
            desc = data.get('desc')
            duration = data.get('duration')
            price = data.get('price')
            instructor = data.get('instructor')
            topics = data.get('topics')

            # Validate the required fields
            if not all([name, short_desc, desc, duration, price, instructor, topics]):
                abort(400, message="Missing required fields")

            # Create a new Course object
            new_course = Course(cn=name, sd=short_desc, de=desc, du=duration, pr=price, i=instructor, t=topics)

            # Add the new course to the database
            db.session.add(new_course)
            db.session.commit()

            return {'status': 'success', 'message': 'Course added successfully'}, 201

        except Exception as e:
            db.session.rollback()
            abort(500, message=f"An error occurred: {str(e)}")        

    

class CourseResource(Resource):
    def get(self, course_id):  # get course by id
        try:
            course = Course.query.filter_by(course_id=course_id).first()
            course = {
                'id': course.course_id,
                'name': course.name,
                'short_desc': course.short_desc,
                'desc': course.desc,
                'duration': course.duration,
                'price': course.price,
                'instructor': course.instructor
            }
            return {'status': 'success', 'data': course}
        except:
            abort(500)

    def delete(self, course_id):
        try:
            course = Course.query.filter_by(course_id=course_id).first()
            db.session.delete(course)
            db.session.commit()
            return {'status': 'success', 'message': 'Course deleted successfully'}, 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=f"An error occurred: {str(e)}") 

class StudentCourseResource(Resource):
    def get(self, student_id):  # get courses taken by student 
        try:
            courses=StudentCourse.query.filter_by(student_id=student_id).all()
            cl=[]
            for c in courses:
                cl.append(c.course_id)
            return {'status':'success', 'data': cl}
        except:
            abort(500)   
    
    def post(self):    # add student-course entry
        try:
            pass
        except:
            abort(500)       

class QuestionResource(Resource):
    def get(self, course_id):
        pass



api.add_resource(LoginAPI, '/api/login')
api.add_resource(SignupAPI, '/api/signup')
api.add_resource(CourseAllResource, '/api/courses')
api.add_resource(CourseResource, '/api/course/<int:course_id>')
api.add_resource(StudentCourseResource, '/api/student/course/<int:student_id>')
api.add_resource(QuestionResource, '/api/question/<int:q_type>/<int:course_id>')