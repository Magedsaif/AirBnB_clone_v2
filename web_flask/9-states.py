#!/usr/bin/python3
"""Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """states_list."""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>')
def states_by_id(id):
    """States_by_id."""
    obj = None
    notfound = True
    for state in storage.all(State).values():
        if state.id == id:
            obj = state
            notfound = False
            break
    return render_template("9-states.html", id=id,
                           state=obj, notfound=notfound)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
