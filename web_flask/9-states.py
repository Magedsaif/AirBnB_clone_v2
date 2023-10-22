#!/usr/bin/python3
"""Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states')
def states():
    """States route."""
    data = storage.all(State)
    return render_template("9-states.html",
                           states=data)


@app.route('/states/<id>')
def states_by_id(id):
    """States_by_id route."""
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
