#!/usr/bin/env python3

from flask import Flask,request,render_template,Response,redirect
from yaml import load as yload,FullLoader
from os.path import exists,join
from random import random
from json import dumps
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response


def create_app():
    app = Flask(__name__,
                static_folder='static')

    # Uncomment and edit the following for app to be mounted under a prefix
    # See `templates/base.html` for usage of `for_url(...)`
    #app.wsgi_app = DispatcherMiddleware(
    #    Response('Not Found', status=404),
    #    {
    #        '/prefix': app.wsgi_app
    #    }
    #)

    config_path = join(app.root_path, 'config.yml')
    if exists(config_path):
        app.config.update(
            yload(open(config_path), Loader=FullLoader))

    app.jinja_env.line_statement_prefix = '#'

    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')


