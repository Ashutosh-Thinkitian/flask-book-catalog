from flask import render_template, request, flash, url_for, redirect
from app.auth.forms import RegistrationForm, LoginForm       # RegistrationForm class in forms.py
from app.auth import authentication as at       # Blueprint
from app.auth.models import User

from flask_login import login_user, logout_user, login_required, current_user
from app.catalog import main

@at.route('/register/', methods=['GET', 'POST'])     # methods get and post for submit the form and default method is GET - doesnt need to mentioned
def register_user():
    """
    name=None
    email=None
    form = RegistrationForm()

    if request.method == 'POST':
        # capturing data
        name = form.name.data
        email = form.email.data

    return render_template('registration.html', form=form, name=name, email=email)      # get request
    """
    if current_user.is_authenticated:  # if user is already log in
        flash('You are Already Logged IN')
        return redirect(url_for('main.display_books'))
    form = RegistrationForm()

    # post request when user click on submit button
    #    check post method and data validation both in form.validate_on_submit()
    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        # if is true then
        flash('Registration Successful')
        return redirect(url_for('authentication.do_the_login'))       # at is instance of blueprint

    return render_template('registration.html', form=form)  # get request -> display form

@at.route('/login', methods=['GET', 'POST'])
def do_the_login():
    if current_user.is_authenticated:   # if user is already log in
        flash('You are Already Logged IN')
        return redirect(url_for('main.display_books'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Entered wrong Username or Password, Please check and try again.')
            return redirect(url_for('authentication.do_the_login'))

        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('main.display_books'))
    return render_template('login.html', form=form)

# log out route
@at.route('/logout')
@login_required
def log_out_user():
    logout_user()   # delete the data from session
    return redirect(url_for('main.display_books'))

#    for 404 error handling
@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
