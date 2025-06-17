from .enrollment_controller import enrollment_bp

def register_route(app):
    app.register_route(enrollment_bp)