#!/usr/bin/env python3

from flask import Flask,request,render_template,Response,redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from sqlalchemy_utils.functions import database_exists
from sqlalchemy import func,and_
from yaml import load as yload,FullLoader
from os.path import exists,join
from model import DatasetType,Dataset,Tag,TagType,Status,Text,TaggerType,Tagger,db,DatasetTypeView,DatasetView,TextView,TagTypeView,TagView,TaggerView,TaggerTypeView
from utils import tag_content
from collections import Counter
from random import random
from json import dumps


def create_app():
    app = Flask(__name__)

    #app.config.from_yaml(app.root_path)
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


