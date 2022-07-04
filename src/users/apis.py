import json
from flask import Blueprint, jsonify, request
from database import db
from users.models import User

users = Blueprint('users', __name__)

@users.route('/users')
def list_users():
    users = User.query.all()
    users_json = []
    for user in users:
        users_json.append({"id": user.id, "username": user.username, "email": user.email})
    return jsonify(users_json)

@users.route('/user/<id>')
def user_details(id):
    user = User.query.get(id)
    users_json = {"id": user.id, "username": user.username, "email": user.email}
    return jsonify(users_json)

@users.route('/user', methods=["POST"])
def create_user():
    try:
        data = json.loads(request.data)
        print(data)
        user = User(username=data["username"], email=data["email"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"success": True})
    except Exception as e:
        print(e)
        return jsonify({"success": False})