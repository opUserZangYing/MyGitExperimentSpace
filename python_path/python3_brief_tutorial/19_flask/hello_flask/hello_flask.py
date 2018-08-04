#!/usr/bin/env python3
# -*- utf-8 -*-
import flask
APP=flask.Flask(__name__)
@APP.route('/')
def index():
    """the page of /"""
    return flask.render_template('index.html')

@APP.route('/hello/<name>')
def hello(name):
    return flask.render_template('hello.html',name=name)

if __name__=='__main__':
    APP.debug=True
    APP.run()