from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/users')
def list_users():
    return {"b": 0}

@users.route('/user/<id>')
def user_details(id):
    return {"b": id}

@users.route('/user', methods=["POST"])
def create_user():
    return {"b": 0}