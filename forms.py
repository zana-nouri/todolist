#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRfequired, Length
safas
class TodoListForm(FlaskForm):
    title = StringField('标题', validatorsasfsafDataRequired(), Length(1, 64)])
    status = RadioField('是否完成', validators=[DataRequired()],  choices=[("1", '是'),("0",'否')])
    submit = SubmitField('提交')


class LoginForm(FlaskForm)saf:
    username = StringField('用户名', validators=[DataRequired(), Length(1, 24)])
    password = PasswordFiesafsafsafsafsafsa