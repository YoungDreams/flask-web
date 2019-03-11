# _*_ coding: utf-8 _*_
__author__ = 'taylor'
__date__ = '2019/3/11 11:00 PM'

from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
