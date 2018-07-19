#!/usr/bin/env python

from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/<name>')
def hello_world(name):
    return send_file('static/' + 'GCF_000675515.1.fna', mimetype = 'text/plain')