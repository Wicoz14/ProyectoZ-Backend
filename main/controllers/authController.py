from flask import request, jsonify, make_response
from main.configurations.config import SECRET_KEY
from  werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt
from main.models.user import User
from main.decorates.authDecorator import token_required
from main.configurations.database.db import db_session
from main.dtos.response import Response
from main.dtos.token import Token

# route for logging user in
def login():
    # obtener parametros
    auth = request.form

    responseData = Response()
    tokenDto = Token()

    if not auth or not auth.get('username') or not auth.get('password'):
        # construir respuesta
        responseData.success = False
        responseData.msg = 'Bad request'

        # respuesta Bad request
        return make_response(
            jsonify(responseData.json()),
            400
        )
  
    user = User.query.filter_by(username = auth.get('username')).first()
  
    if not user:
        # construir respuesta
        responseData.success = False
        responseData.msg = 'Unauthorized'


        # respuesta inautorizado
        return make_response(
            jsonify(responseData.json()),
            401
        )
  
    if check_password_hash(user.password, auth.get('password')):
        # generar token
        tokenDto.token = jwt.encode({
            'id': user.id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, SECRET_KEY, algorithm='HS256')

        #  construir respuesta
        responseData.success = True
        responseData.msg = 'Ok'
        responseData.data = tokenDto.json()
  
        return make_response(
            jsonify(responseData.json()),
            200
        )
    else:
        # construir respuesta
        responseData.success = False
        responseData.msg = 'Unauthorized'

        # respuesta inautorizado
        return make_response(
            jsonify(responseData.json()),
            401
        )

@token_required
def signup(self):
    # obtener parametros
    data = request.form

    username = data.get('username')
    names = data.get('names')
    lastNames = data.get('lastNames')
    email = data.get('email')
    password = data.get('password')
  
    # Verificar si alguien ya tiene ese username o email
    user = User.query.filter_by(username = username).first()
    if not user:
        # database ORM object
        user = User(
            username = username,
            names = names,
            lastNames = lastNames,
            email = email,
            password = generate_password_hash(password)
        )
        # insert user
        db_session.add(user)
        db_session.commit()
  
        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)