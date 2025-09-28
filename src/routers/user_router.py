from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

from configuration.extensions import jwt
from configuration.injections import get_user_service
from models.user import CreateUser, LoginUser

user_bp = Blueprint('users', __name__, url_prefix='/users')


@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    user = CreateUser(**data)
    user_service = get_user_service()
    user_data = user_service.register_user(user)

    access_token = create_access_token(identity=user_data['id'])

    return jsonify({
        'user_id': user_data['id'],
        'username': user_data['username'],
        'email': user_data['email'],
        'access_token': access_token
    }), 201



@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = LoginUser(**data)
    user_service = get_user_service()
    user_data = user_service.verify_user(user)
    access_token = create_access_token(identity=user_data['id'])
    return jsonify({
        'user_id': user_data['id'],
        'username': user_data['username'],
        'email': user_data['email'],
        'access_token': access_token,
        'message': f'Welcome {user_data["username"]}!'
    }), 200



@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    user_service = get_user_service()
    jti = jwt_payload['jti']
    return user_service.is_jti_blacklisted(jti)


@user_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    user_service = get_user_service()
    jti = get_jwt()['jti']
    user_service.blacklist_token(jti)
    return jsonify({
        'message': 'Logout successful',
    }), 200




