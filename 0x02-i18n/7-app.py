#!/usr/bin/env python3
""" module 7-app.py with a basic Flask app and Babel setup """

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
""" instantiates Babel object """
babel = Babel(app)

""" mock database user table """
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    elif g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


""" initializes the Babel object and passes in a locale_selector function """
babel.init_app(app, locale_selector=get_locale)


def get_user():
    """ returns a user dictionary or None if the ID cannot be found or
      if login_as was not passed """
    userId = request.args.get('login_as')
    try:
        return users[int(userId)]
    except (KeyError, ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """ find a user if any, and set it as a global on flask.g.user """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    if 'timezone' in request.args:
        try:
            timezone = pytz.timezone(request.args.get('timezone'))
            return timezone.zone
        except pytz.UnknownTimeZoneError:
            pass
    elif g.user and g.user['timezone']:
        try:
            timezone = pytz.timezone(g.user['timezone'])
            return timezone.zone
        except pytz.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Basic Flask App """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
