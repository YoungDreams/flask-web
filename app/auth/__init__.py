# _*_ encoding:utf-8 _*_
__author__ = 'taylorlee'

from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes