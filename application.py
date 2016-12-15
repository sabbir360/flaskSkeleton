"""
Flask kickstart from here with routing rules.
"""
from app import APP
# Import modules. Modules generally ends with _mod
from dbengine import DB_SESSION
from home_mod.controller import HOME_R

# put routes here. url_prefix will define whether its start from x or y!
APP.register_blueprint(HOME_R, url_prefix="/")


@APP.teardown_appcontext
def shutdown_session(exception=None):
    """
    Initiate while ending any request each time.
    """
    if exception:
        print("---------EXCEPTION---------")
        print(exception)
    DB_SESSION.remove()


APPLICATION = APP
