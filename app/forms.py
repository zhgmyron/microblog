# -*- coding: UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired
class LoginForm(Form):
    openid = StringField('openid',validators=[DataRequired()])
    remeber_me = BooleanField('remember_me', default=False)
