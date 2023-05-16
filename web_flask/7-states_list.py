#!/usr/bin/python3
"""Start a flask application.
Routes:
display a HTML page: (inside the tag BODY)
"""
from models import storage
from flask import Flask, abort
from flask import render_template
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Display states sorted by name
    """
    states_dict = storage.all(State)
    list_sorted = sorted(states_dict.values(), key=lambda obj: (obj.name))
    return render_template("7-states_list.html", list=list_sorted)


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
