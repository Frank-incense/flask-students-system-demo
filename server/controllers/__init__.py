from .enrollment_controller import enrollment_bp
from .student_courses import student_bp
from .students_controller import student_blueprint

def register_route(app):
    app.register_blueprint(enrollment_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(student_blueprint)