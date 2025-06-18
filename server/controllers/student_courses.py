from flask import Blueprint, make_response
from models import Student

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/students/courses/<int:id>')
def get_student_courses(id):
    student = Student.query.filter_by(id=id).first()
    courses = student.courses
    if len(courses):
        res = make_response([course.to_dict() for course in courses], 200)
        return res
    
    return make_response({"Message": "Student not enrolled in any course"}, 204)
