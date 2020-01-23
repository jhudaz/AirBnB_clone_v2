#!/usr/bin/python3
""" script to start the server """
from models import storage
from models import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    storage.close()


@app.route('/states', defaults={'id':None})
@app.route('/states/<id>', strict_slashes=False)
def states(id):
    states = storage.all('State')
    return render_template("9-states.html", id=id, states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

