"""
MVC : example blueprint for large app
"""

from flask import Blueprint, abort
from jinja2 import TemplateNotFound

from helpers.template import Template

from home_mod.model import User

HOME_R = Blueprint('home', __name__, template_folder='templates')

@HOME_R.route('/<page>')
def show(page):
    '''
    for example buddy
    '''
    try:
        if page:
            return "You hit: "+page
        return "Blueprint"
    except TemplateNotFound:
        abort(404)

@HOME_R.route("/")
def home():
    """
    Home page
    """
    template = Template()
    template.set_title("RoR Check.")
    return template.render("/ror/index", entries=User().query.all())
