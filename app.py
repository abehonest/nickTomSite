#!/usr/bin/env python

from flask import Flask, request, make_response, render_template, redirect, json
from flask import url_for, abort, session
import sys

app = Flask(__name__, template_folder='./templates/')


@app.route('/', methods=['GET'])
def index():

    html = render_template('index.html')
    response = make_response(html)

    return response
