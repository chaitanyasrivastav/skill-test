import json
from flask import Blueprint, jsonify, request
from database import db
from questions.models import Question

questions = Blueprint('questions', __name__)

@questions.route('/questions')
def list_questions():
    questions = Question.query.all()
    questions_json = []
    for question in questions:
        questions_json.append({"id": question.id, "text": question.text, "topic": question.topic, "weightage": question.weightage})
    return jsonify(questions_json)

@questions.route('/question/<id>')
def question_details(id):
    question = Question.query.get(id)
    questions_json = {"id": question.id, "text": question.text, "topic": question.topic, "weightage": question.weightage}
    return jsonify(questions_json)

@questions.route('/question', methods=["POST"])
def create_question():
    try:
        data = json.loads(request.data)
        print(data)
        question = Question(id=data["id"], text=data["text"], topic=data["topic"], weightage=data["weightage"])
        db.session.add(question)
        db.session.commit()
        return jsonify({"success": True})
    except Exception as e:
        print(e)
        return jsonify({"success": False})