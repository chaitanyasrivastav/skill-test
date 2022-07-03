from flask import Flask
from users.apis import users
from questions.apis import questions

app = Flask(__name__)
app.register_blueprint(users)
app.register_blueprint(questions)