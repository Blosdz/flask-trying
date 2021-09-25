#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return"hello world"
@app.route("/<string:name>/<int:date>/<int:year>")
def hello(name,year,date):
    return f"hello, {name},tu edad es {date}, naciste en {year}"
