#!/usr/bin/env python3
'''Activates babel on the flask app'''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''contains i18n configs'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''Determines the best language match for a locale'''
    return request.accept_languages.best_match(app.Config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_world():
    '''Testing'''
    return render_template('2-index.html')


if __name__ == "__main__":
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
