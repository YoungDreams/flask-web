# _*_ encoding:utf-8 _*_
__author__ = 'taylorlee'


from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes