#!/usr/bin/env python3
'''Gets user locale to enable translation'''

import pytz
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''contains i18n configs'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }


def get_user():
    '''gets user based on the login_as parameter'''
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    '''set user in the global variable'''
    g.user = get_user()


@babel.localeselector
def get_locale():
    '''Determines the best language match for a locale'''
    # locale from url parameters
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    # locale from user settings
    if g.user and 'locale' in g.user:
        user_locale = g.user['locale']
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    # locale from request header
    request_locale = request.headers.get('Accept-Language')
    if request_locale:
        lang = request_locale.split(',')[0].split(';')[0].strip()
        if lang in app.config['LANGUAGES']:
            return lang

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    '''Determines the best timezone for a request'''
    url_time = request.args.get('timezone')
    if url_time:
        try:
            pytz.timezone(url_time)
            return url_time
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and 'timezone' in g.user:
        user_timezone = g.user['timezone']
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.execeptions.UnknownTimezoneError:
                pass

    return 'UTC'


@app.route('/', strict_slashes=False)
def hello_world():
    '''renders html template to the webpage'''
    timezone = get_timezone()
    current_time = datetime.now(pytz.timezone(timezone))
    current_time = format_datetime(current_time, format='full') 
    return render_template('index.html', current_time=current_time)


if __name__ == "__main__":
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
