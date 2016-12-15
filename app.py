"""
Initialize server or anything you like.
"""
# import sqlite3
# from flask import render_template, g
from flask import Flask
# from config import DATABASE_PATH
# from dbengine import DB_SESSION

APP = Flask(__name__)

APP.config.from_object(__name__)
# APP.config.update(dict(
#     DATABASE=DATABASE_PATH
# ))

APP.config.from_envvar('FLASKR_SETTINGS', silent=True)

# def connect_db():
#     """
#     Connects to the specific database.
#     """
#     sqlite_db = sqlite3.connect(APP.config["DATABASE"])
#     sqlite_db.row_factory = sqlite3.Row
#     return sqlite_db

# def get_db():
#     """Opens a new database connection if there is none yet for the
#     current application context.
#     """
#     if not hasattr(g, 'sqlite_db'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db

# @APP.route('/')
# def hello_world():
#     '''
#     Test
#     '''
#     dbcon = get_db()
#     cur = dbcon.execute('SELECT name, email, id from users')
#     entries = cur.fetchall()
#     return render_template("/ror/index.html", entries=entries)

# @APP.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if error:
#         print(error)
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()

# import pdb; pdb.set_trace()
print(APP.url_map)
