#!/usr/bin/python3
"""
script to starts a flask web application.
The application listening on 0.0.0.0, port 5000.
each request removes the current SQLAlchemy Session
Routes:
/states_list: display a HTML page: (inside the tag BODY)
H1 tag: "States"
UL tag: with the list of all State objects present in
DBStorage sorted by name (A->Z) tip

LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """close current session of sqlalchemy"""
    storage.close()


@app.route('/states_list')
def states_list():
    """
    returns an HTML page with a list of all State objects in DBStorage.
    States to be sorted by name.
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

