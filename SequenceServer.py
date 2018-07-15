#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/<name>')
def hello_world(name):
    return 'Hello %s!' % name