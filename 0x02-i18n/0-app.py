#!/usr/bin/env python3
'''Creates the flask app'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''Testing'''
    return render_template('0-index.html')


if __name__ == "__main__":
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
