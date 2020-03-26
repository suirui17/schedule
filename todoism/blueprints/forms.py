from wtforms import StringField, SubmitField, PasswordField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired('username is null')])
    password = PasswordField('password', validators=[DataRequired('password is null')])
    submit = SubmitField('Login in')


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired('username is null')])
    password = PasswordField('password', validators=[DataRequired('password is null'), Length(8, 128)])
    password_again = PasswordField('password again', validators=[DataRequired()])
    submit = SubmitField('Sign up')


class ItemForm(FlaskForm):
    begin_time = DateField('begin time', validators=[DataRequired()])
    end_time = DateField('end time')
    body = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('submit')

