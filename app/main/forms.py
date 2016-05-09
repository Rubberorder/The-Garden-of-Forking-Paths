# -*- coding:utf8 -*-
#encoding = utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from flask.ext.pagedown.fields import PageDownField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('Secret', validators=[Required()])
    submit = SubmitField('Log in')
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep logged in')

class PostForm(Form):
	title = StringField(u'标题', validators=[Required()])
	body = PageDownField(u'文章', validators=[Required()])
	submit = SubmitField(u'提交')
