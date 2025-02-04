#!/usr/bin/python3
"""Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
