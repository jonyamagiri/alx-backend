#!/usr/bin/env python3
""" module 0-app.py with a basic Flask app """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Basic Flask App """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
