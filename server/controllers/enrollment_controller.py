from models import Enrollment, db
from flask import Blueprint, jsonify, make_response, request

enrollment_bp = Blueprint('enrollment_bp', __name__)

@enrollment_bp.route('/enrollments',methods=['GET','POST'])
def enrollments():
    if request.method == 'GET':
        enrollments = Enrollment.query.all()
        if len(enrollments) > 0:
            response_body = [enrollment.to_dict() for enrollment in enrollments]
            response_stat = 200
            return make_response(response_body, response_stat)
        else:
            response_body = {"error": "Enrolments not found"}
            response_stat = 404
            return make_response(response_body, response_stat)

    elif request.method == 'POST':
        data = request.get_json()
        try: 
            newEnrollment = Enrollment(
                _student_id = data.get("student_id"),
                _course_id = data.get("course_id")
            )

            db.session.add(newEnrollment)
            db.session.commit()

            res = newEnrollment.to_dict()
            stat = 200
            return make_response(res, stat)
        except ValueError as err:
            res = {"error": "Enrollement failed",
                   "Message":[f"{err}"]}
            stat = 400
            return make_response(res, stat)

@enrollment_bp.route('/enrollments/<int:id>', methods=['DELETE'])
def del_enrollments(id):
    enrollment = Enrollment.query.filter_by(id=id).first()
    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
    else:
        res = make_response(
            {'error': 'Enrollment not found'}, 404
        )
        return res

    res = make_response('', 204)
    return res