import flask
from flask import Response, request, send_file, Flask
import json
import sqlite3
import csv

app = flask.Flask(__name__)


@app.route('/')
def index():
	return flask.render_template('aboutUs.html')
if __name__ == '__main__':
    app.debug=True
    app.run()
