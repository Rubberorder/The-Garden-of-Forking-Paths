# -*- coding:utf-8 -*-
#encoding = utf-8
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms import ValidationError
from wtforms.validators import Required
from ..models import User

class LoginForm(Form):
	name = StringField("Username", validators=[Required()])
	password = PasswordField("Password", validators=[Required()])
	remember_me = BooleanField("Remember me")
	submit = SubmitField("Login")