#coding=utf-8

from flask import Blueprint
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def index():
    return '<h1>Hello, this is admin blueprint</h1>'