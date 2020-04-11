import flask
from flask import Flask, request, g
import sqlite3 as sql

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect("library.db")
    db.row_factory = sql.Row
    return db

from views.login import *

if __name__ == '__main__':
	app.run(use_reloader=True)