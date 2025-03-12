from flask import Blueprint, jsonify, request, abort
from app.services.user_service import UserService
from app.utils.database import get_db
from app.models.user_model import User

user_bp = Blueprint('user', __name__, url_prefix='/')

@user_bp.route('/', methods=['GET'])
def get_users():
    db = get_db()
    users = UserService.get_all_users(db)
    return jsonify(users)

@user_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id == 'favicon.ico':
        return '', 204
    db = get_db()
    user = UserService.get_user_by_id(db, user_id)
    return jsonify(user)

@user_bp.route('/', methods=['POST'])
def create_user():
    db = get_db()
    data = request.get_json()

    try:
        user_data = User(**data)
    except Exception as e:
        abort(400, description=str(e))

    user = UserService.create_user(db, user_data.model_dump())
    return jsonify(user), 201

@user_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    db = get_db()
    data = request.get_json()

    try:
        user_data = User(**data)
    except Exception as e:
        abort(400, description=str(e))

    user = UserService.update_user(db, user_id, user_data.model_dump())
    return jsonify(user)

@user_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    db = get_db()
    UserService.delete_user(db, user_id)
    return '', 204