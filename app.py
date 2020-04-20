import flask
from flask import Flask, request, g
import sqlite3 as sql
from flask_cors import CORS, cross_origin


app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect("library.db")
    db.row_factory = sql.Row
    return db

from views.login import *
from views.books import *
from views.member import *

if __name__ == '__main__':
	app.run(use_reloader=True)