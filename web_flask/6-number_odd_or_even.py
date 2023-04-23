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
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def print_template(n):
    """prints a HTML page only if n is an integer"""
    return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>')
def print_odd_or_even(n):
    """ display if number is even or odd """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
