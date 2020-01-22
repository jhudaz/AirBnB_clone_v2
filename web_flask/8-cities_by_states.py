#!/usr/bin/python3
""" script to start the server """
from models import storage
from models import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states():
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
