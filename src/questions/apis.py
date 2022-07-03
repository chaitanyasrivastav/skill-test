from flask import Blueprint

questions = Blueprint('questions', __name__)

@questions.route('/questions')
def list_questions():
    return {"b": 0}

@questions.route('/question/<id>')
def question_details(id):
    return {"b": id}

@questions.route('/question', methods=["POST"])
def create_question():
    return {"b": 0}