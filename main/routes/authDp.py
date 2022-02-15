from flask import Blueprint
from main.controllers.authController import login, signup

authBp = Blueprint('auth_bp', __name__)

authBp.route('/login', methods=['POST']) (login)

authBp.route('/signup', methods=['POST']) (signup)