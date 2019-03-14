# _*_ encoding:utf-8 _*_
__author__ = 'taylorlee'


from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers