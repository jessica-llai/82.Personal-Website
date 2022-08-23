from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Done')


class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Done')


