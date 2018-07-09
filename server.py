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

@app.route('/')
def homepage():
    """
    Home view of my project
    """
    results = request.args.get("")
    return render_template("")


if __name__ == "__main__":
    app.run(debug=True)



