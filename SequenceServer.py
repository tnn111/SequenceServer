#!/usr/bin/env python

from flask import Flask, send_file

app = Flask(__name__)

BASE = '/Users/torben/Dropbox/Work/Python/SequenceServer/static/'

@app.route('/')
def index():
    return 'In the beginning there was the Void.'

@app.route('/<name>')
def return_file(name):
    xxx, yyy, zzz, version = name[4:7], name[7:10], name[10:13], name[14:]
    if version:
      file_name = xxx + '/' + yyy + '/' + zzz + '/' + \
                  'GCF_' + xxx + yyy + zzz + '.' + version + '/' + \
                  'GCF_' + xxx + yyy + zzz + '.' + version + '.fna.gz'
    app.logger.info('File name is: ' + file_name)
    return send_file(BASE + file_name, as_attachment = True)
