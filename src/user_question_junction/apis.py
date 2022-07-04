import json
from flask import Blueprint, jsonify, request
from database import db
from user_question_junction.models import UserQuestion
from users.models import User
from questions.models import Question

user_questions = Blueprint('user_questions', __name__)

@user_questions.route('/user/<uid>/question/<qid>/scores')
def list_user_questions(uid, qid):
    user_questions = UserQuestion.query.filter_by(user_id=uid, question_id=qid)
    user_questions_json = []
    for user_question in user_questions:
        user_questions_json.append({"question_id": user_question.question_id, "score": user_question.score, "lastAttempted": user_question.last_attempt})
    return jsonify(user_questions_json)


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

@user_questions.route('/user/<uid>/question/<qid>/avgscore')
def list_user_question_avg_score(uid, qid):
    user_questions = UserQuestion.query.with_entities(db.func.avg(UserQuestion.score).label("avg_score")).filter_by(user_id=uid, question_id=qid).first()
    return jsonify({"avg_score": user_questions.avg_score})