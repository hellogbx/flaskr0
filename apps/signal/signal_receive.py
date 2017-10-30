#coding=utf-8
from flask import template_rendered, request_started
from flask_sqlalchemy import models_committed, before_models_committed
from apps.blog.models import app, db, Entries

@template_rendered.connect_via(app)
def log_template_renders(app, template, context, **extra):
    print "模版保存了"


@before_models_committed.connect_via(app)
def model_saved_before_test(app, changes, **extra):
    print "model保存了之前"
    print changes[0][0].title
    print changes[0][0].text


@models_committed.connect_via(app)
def model_saved_test(app, changes, **extra):
    print "model保存了之后"


@request_started.connect_via(app)
def request_start_test(app):
    print "请求开始了"