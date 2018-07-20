#!/usr/bin/env python

from flask import Flask, send_file

app = Flask(__name__)

BASE = '/Users/torben/Dropbox/Work/Python/SequenceServer/static/'

@app.route('/')
def index():
    return 'Index'
    
@app.route('/<name>')
def hello_world(name):
    print(os.listdir(BASE))
    return send_file(BASE + 'GCF_000675515.1.fna.gz')