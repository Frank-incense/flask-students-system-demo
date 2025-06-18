from flask import Flask, send_file, request, jsonify
from flask_cors import CORS
from models import db, Student, Course
from controllers import register_route
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config.from_prefixed_env()

db.init_app(app)
migration = Migrate(app, db)

@app.before_request
def beforerequest():
    authed = False
    if request.path.startswith("/uploads") and authed == False:
        return "Prouted route. you need to be logged in", 403


@app.route("/")
def home():
    return send_file("./static/index.html")

@app.route("/uploads/<string:filename>")
def uploads(filename):
    return send_file(f"./uploads/{filename}")


@app.route('/courses', methods=['GET'])
def courses():
    courses = Course.query.all()
    courses_data = [course.to_dict() for course in courses]
    return jsonify(courses_data), 200



@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_course = Course()
    new_course.name = data['name']
    db.session.add(new_course)
    db.session.commit()
    
    return jsonify(new_course.to_dict()), 201

register_route(app=app)

if __name__ =='__main':
    app.run(port=5555, debug=True)
# MISSING MODULE psycopg2

