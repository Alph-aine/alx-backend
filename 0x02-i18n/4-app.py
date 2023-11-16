#!/usr/bin/env python3
'''Gets user locale to enable translation'''

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
    if 'locale' in request.args:
        requested_locale = request.args['locale']
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_world():
    '''renders html template to the webpage'''
    return render_template('4-index.html')


if __name__ == "__main__":
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
