from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.security import generate_password_hash, check_password_hash
# from model import User, User_Search, Search, Outlet, connect_to_db, db
# import pytz
import os
import requests

app = Flask(__name__)

app.secret_key = 'ABC'

app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True
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

    data = requests.get("https://www.eventbriteapi.com/v3/events/search/?location.address=san+francisco&location.within=30mi&price=free&start_date.keyword=next_week&token=ZAKXWP2CDSBC2SS7RVYQ")

    all_events = data.json()

    week_events = all_events['events']

    content = []

    for i in range(len(week_events)):
            title = (week_events[i].get('name')['text'] or " ").encode('utf-8')
            about = (week_events[i].get('description')['text'] or " ").encode('utf-8')
            url = (week_events[i].get('url') or " ").encode('utf-8')
            time = (week_events[i].get('start')['local'] or " ").encode('utf-8')
            event = " - {} - description: {} url: {} time: {} | \n".format(title, about, url, time)
            event = unicode(event, 'utf-8')
            content.append(event)

    # print title + "\n", "description: " + about + "\n", "url: " + url + "\n", "time: " + time

    # content = unicode(content)
    # final_events = content.normalize("NFKD", u'\xa0')

    # final = "\n\n\n\n\n\n\n|||||||||||||||||||".join(content

    return render_template("home.html",
                            data=content)

# =============================================================================
# This/Next Month view

@app.route('/thismonth')
def this_months_events():
    """
    Lists all events for the current month
    """

    return render_template("thismonth.html")

# @app.route('/upcoming')
# def upcoming_events():
#     """
#     Lists all events for the upcoming month
#     """
#     results = request.args.get("")
#     return render_template("upcoming.html")

#=============================================================================

@app.route('/<user_id>')
def user_profile():
    """
    Displays all events added to calendar by a given user. Other people
    can not view each other user profiles - it is for user to keep track personally
    of past events
    """

    results = request.args.get("")
    return render_template("user.html")

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
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    # DebugToolbarExtension(app)
    # connect_to_db(app)
    app.run(port=5000, host='0.0.0.0')



