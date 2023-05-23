#!/usr/bin/env python3
""" module 4-app.py with a basic Flask app and Babel setup """

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
""" instantiates Babel object """
babel = Babel(app)


class Config(object):
    """ config class for Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


""" set above class object as the configuration for the app """
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ gets best match for supported languages in locales """
    if 'locale' in request.args and request.args.get(
            'locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Basic Flask App """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
