from jinja2 import StrictUndefined
from flask import flask
from flask import request, render_template, redirect, flash, session, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
# from datetime import datetime
# import pytz
# import requests


app = Flask(__name__)

#A function that returns a web response is a VIEW
# our function will return an HTML string
# '/' is a python decorator that maps directly to the URL that the user requested
# GET vs POST: Get does not change, Post does!
# GET to view flights, POst to submit order
# GET is implied by default on an HTML form AND default in Flask Routes
# request.args.get() is for GET
# request.form.get() is for POST

# Currently are NO HTML forms to supply email/password too. Also NO data model / data base to hold info

# =============================================================================
# Home page displaying this weeks events

@app.route('/')
def homepage():
    """
    Home view of my project
    """


    results = request.args.get("")
    return render_template("")

# =============================================================================
# This/Next Month view

@app.route('/thismonth')
def this_months_events():
    """
    Lists all events for the current month
    """

    results = request.args.get("")
    return render_template("")

@app.route('/upcoming')
def upcoming_events():
    """
    Lists all events for the upcoming month
    """
    results = request.args.get("")
    return render_template("")

#=============================================================================
# User Profile / user list

@app.route('/users/<user_id>')
def user_profile(user_id):
    """
    Displays all events added to calendar by a given user. Other people
    can not view each other user profiles - it is for user to keep track personally
    of past events
    """

    results = request.args.get("")
    return render_template("")

@app.route('/users')
def all_users():
    """Show list of users"""
# create a variable users that contains all of the users in database
    users = User.query.all()
    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def user_page(user_id):
    """ Show user profile """

    # user = User.query.filter_by(user_id=user_id).options(
    #     db.joinedload('ratings')).one()
    # return render_template('user.html', user=user)

# =============================================================================
# User Login / User Logout

@app.route('/login', methods=['GET']) 
def login_form():
    """
    Displays Login Form (if error logging in) and redirects from modal to login 
    """


    return render_template('login.html')

@app.route('/login', methods=['POST']) 
def user_login():
    """Login user"""

# gets email and password from form
    email = request.form.get('email')
    password = request.form.get('password')
# checks if user is in database
    user = User.query.filter(User.email == email).first()
    if user is None:
        flash('User not found')
        return redirect('/')
# if passwords match, adds user to session and redirects to homepage
    if check_password_hash(user.password, password):
        session['user_id'] = user.user_id
        flash('Logged in as {}'.format(user.email))
        return redirect('/')
# if passwords don't match, redirect to login page
    flash('Invalid password')
    return redirect('/')

@app.route('/logout')
def user_logout():
    """Logout user"""
# delete user information out of session
    if 'user_id' in session:
        del session['user_id']
        flash ('Logged out')
# redirects to homepage
    return redirect('/')

# =============================================================================
# Register New User

@app.route('/register', methods=['GET'])
def register_form():
    """Display register form if modal fails"""

    return render_template('register_user.html')

@app.route('/register', methods=['POST'])
def register_user():
    """ Register New User """
# get email and password from HTML form
    email = request.form.get('email')
    password = request.form.get('password')
# hash passwords
    hashed_value = generate_password_hash(password)
# check to see if uses exists - if not, create a new User instance with input. Add user to database and to session
    if User.query.filter(User.email == email).first() is None:
        user = User(email=email, password=hashed_value)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.user_id
        flash('Registered as {}'.format(email))
        return redirect('/')
# if user is found in database, flash message and redirect to form
    flash('User already exists - Please use different Email')
    return redirect('/register')

if __name__ == "__main__":
    app.run(debug=True)



