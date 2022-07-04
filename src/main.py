from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from users.apis import users
from questions.apis import questions
from user_question_junction.apis import user_questions
from database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.init_app(app)
    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = '/static/skill_test.json'  # Our API url (can of course be a local resource)

    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL,
        config={
            'app_name': "Test application"
        },
    )
    app.register_blueprint(swaggerui_blueprint)
    app.register_blueprint(users)
    app.register_blueprint(questions)
    app.register_blueprint(user_questions)
    return app