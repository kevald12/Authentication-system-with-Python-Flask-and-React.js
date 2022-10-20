"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

#create flask app
api = Blueprint('api', __name__)


@api.route('/signup', methods=['POST'])
def post_user():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    new_user = User(email = email, password = password, is_active = True)
    db.session.add(new_user)
    db.session.commit()
    response_body = {
        "msg": "Usuario creado exitosamente"
    }
    return jsonify(response_body), 200

