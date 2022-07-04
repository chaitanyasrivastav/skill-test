from flask import Flask
from users.apis import users
from questions.apis import questions
from user_question_junction.apis import user_questions
from database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.init_app(app)
    app.register_blueprint(users)
    app.register_blueprint(questions)
    app.register_blueprint(user_questions)
    return app