#!/usr/bin/python3
"""Flask web application."""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """hello_world."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """C is fun."""
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    app.run()
