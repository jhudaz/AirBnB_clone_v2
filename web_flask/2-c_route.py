#!/usr/bin/python3
""" script to start the server """
from flask import Flask
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
    """c hbnb using arguments"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
