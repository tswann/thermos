__author__ = 'tswann'

from flask_wtf import Form
from wtforms.fields import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, Email, ValidationError
from ..models import User

class LoginForm(Form):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class SignupForm(Form):
    username = StringField ('Username',
                            validators=[
                                DataRequired(), Length(3, 80),
                                Regexp('^[A-Za-z0-9_]{3,}$',
                                       message='Usernames consist of numbers, letters and underscores.')
                            ])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2', message='Passwords must match.')
                             ])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1,120), Email()])

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('There is already a user with this email address.')

    def validate_username(self, username_field):
        if User.get_by_username(username_field.data):
            raise ValidationError('This username is already taken.')