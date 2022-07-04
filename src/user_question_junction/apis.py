import json
from flask import Blueprint, jsonify, request
from database import db
from user_question_junction.models import UserQuestion
from users.models import User
from questions.models import Question

user_questions = Blueprint('user_questions', __name__)

@user_questions.route('/user/<uid>/questions')
def list_user_questions(uid):
    user_questions = UserQuestion.query.filter(user_id=uid)
    user_questions_json = []
    for user_question in user_questions:
        user_questions_json.append({"user_id": user_question.user_id, "question_id": user_question.question_id, "score": user_question.score, "lastAttempted": user_question.last_attempt})
    return jsonify(user_questions_json)

# @user_questions.route('/user/<id>')
# def user_details(id):
#     user = User.query.get(id)
#     users_json = {"id": user.id, "username": user.username, "email": user.email}
#     return jsonify(users_json)

@user_questions.route('/user/<uid>/question/<qid>', methods=["POST"])
def create_user_question(uid, qid):
    try:
        data = json.loads(request.data)
        print(data)
        user = User.query.get(uid)
        question = Question.query.get(qid)
        user_question = UserQuestion(user_id=user.id, question_id=question.id, score=data["score"])
        db.session.add(user_question)
        db.session.commit()
        return jsonify({"success": True})
    except Exception as e:
        print(e)
        return jsonify({"success": False})