from flask import Blueprint, make_response, request
from models import Student, db

student_blueprint = Blueprint('students', __name__)

@student_blueprint.route('/students', methods=['GET', 'POST'])
def students():
    students = Student.query.all()
    if request.method == 'GET':
        if len(students) > 0:
            res = make_response([student.to_dict() for student in students], 200)
            return res
        else:
            return make_response({'Error':'Students not found'}, 404)
    elif request.method == 'POST':
        data  = request.form

        newStudent = Student(
            name= data.get('name')
        )

        db.session.add(newStudent)
        db.session.commit()

        return make_response(newStudent.to_dict(), 201)
        # for attr in data:
        #     setattr()

@student_blueprint.route('/students/<int:id>')
def studentById(id):
    student = Student.query.filter_by(id=id).first()

    if student:
        res = make_response(student.to_dict(), 200)
        return res
    return make_response({'Error':'Student not found'}, 404)