#!/usr/bin/python3
""" Script that starts A Flask web Application
Iy should listen on port 0.0.0.0 5000
Routes:   /: display “Hello HBNB!”
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays Hello HBNH!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
