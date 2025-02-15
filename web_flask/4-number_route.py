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


@app.route('/c/<text>')
def display_c(text):
    """Print 'c' followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def diplay_python(text="is cool"):
    """display "Python" followed by the value of the text variable"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def print_number(n):
    """ number route """
    return '{:d} is a number'.format(n)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
