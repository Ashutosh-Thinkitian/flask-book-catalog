#    import wtforms with fields, submit button
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField

from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError  # For form validation
from app.auth.models import User

# add custom validators for check credential already exists in database or not
def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email is already exists! Please go on login')

def name_exists(form, field):
    user_name = User.query.filter_by(user_name=field.data).first()
    if user_name:
        raise ValidationError('Username is already exists, Please choose unique username')

class RegistrationForm(FlaskForm):  # inheritance with FlaskForm
    name = StringField("Enter Your Name",
                       validators=[DataRequired("Please enter Username"), Length(3, 15, message='Name must be in between 3 to 15 characters'), name_exists])
    email = StringField("Enter Your Email", validators=[DataRequired("Please enter Email"), Email(), email_exists]) # add custom validation function in end
    # StringField ("This is label attribute in html form")

    password = PasswordField("Enter Password:",
                             validators=[DataRequired("Please enter Password"), Length(5, message='Must be at least 5 character/numbers')])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired("Please enter Password again"),
                                                                     EqualTo('password', message='Password must match with confirm password')])

    submit = SubmitField("Register")

# log in form
class LoginForm(FlaskForm):
    email = StringField('Enter Your Email', validators=[DataRequired(), Email()])
    password = PasswordField('Enter Yor Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('Remember Me')
    submit = SubmitField('Log In')
