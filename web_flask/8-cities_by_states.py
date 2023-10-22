#!/usr/bin/python3
"""Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page."""
    list = sorted(storage.all(
        State).values(), key=lambda x: x.name)
    for s in list:
        s.cities.sort(key=lambda x: x.name)
    return render_template("8-cities_by_states.html", sorted_states_list=list)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
