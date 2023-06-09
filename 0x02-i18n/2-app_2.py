#   alternative (The locale_selector function takes a request object as input and returns the best matching locale for the user. The app.config['LANGUAGES'] setting specifies the list of supported languages.)

#!/usr/bin/env python3
""" module 2-app.py with a basic Flask app and Babel setup """

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


def get_locale():
    """ gets best match for supported languages in locales """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


""" initializes the Babel object and passes in a locale_selector function """
babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Basic Flask App """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
