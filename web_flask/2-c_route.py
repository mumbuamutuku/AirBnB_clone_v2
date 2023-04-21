#!/usr/bin/python3
""" Script that starts A Flask web Application
Iy should listen on port 0.0.0.0 5000
Routes:   /: display “Hello HBNB!”
/hbnb: Displays 'HBNB'.
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays Hello HBNH!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
