__author__ = 'sabbir'
# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
application = Flask(__name__)

# Configurations
application.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
# db = SQLAlchemy(app)

# Sample HTTP error handling
@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from application.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
application.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
#  db.create_all()