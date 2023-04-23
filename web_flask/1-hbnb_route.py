#!/usr/bin/python3
"""This script starts a flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def greet():
    """Print Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def greet_two():
    """Print HBNB"""
    return "HBNB"


if __namr__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
