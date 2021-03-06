#!/usr/bin/python3
""" script to start the server """
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """"main content"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """path hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """path c using arguments"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/(<text>)/", strict_slashes=False)
def python(text):
    """path python using arguments"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>/", strict_slashes=False)
def number(n):
    """path number using arguments"""
    return "{} is a number".format(n)


@app.route("/number_template/")
@app.route("/number_template/<int:n>/", strict_slashes=False)
def number_template(n):
    """path number_template using arguments"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
