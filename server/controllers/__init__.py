from .enrollment_controller import enrollment_bp

def register_route(app):
    app.register_blueprint(enrollment_bp)