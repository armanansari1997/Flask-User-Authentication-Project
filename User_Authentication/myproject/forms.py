from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError
from User_Authentication.myproject.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', 'Passwords must match')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registered!') 
    
    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username is already taken!')
