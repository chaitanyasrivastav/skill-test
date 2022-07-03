from flask import Flask
from users.apis import users
from questions.apis import questions
from database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.init_app(app)
    app.register_blueprint(users)
    app.register_blueprint(questions)
    return app