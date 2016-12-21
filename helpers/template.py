"""This script will make some helper to serve templates better."""
from flask import render_template, redirect, request

from config import APP_NAME


class Template():
    """
    A common class to rescue common mistakes while using templates
    """

    title = APP_NAME

    def __init__(self):
        pass

    def set_title(self, title):
        """
        Set a formatted title
        """
        self.title = title + " | " + APP_NAME

    def render(self, template, **context):
        """Renders a template from the template folder with the given
        context.

        :param template_name_or_list: the name of the template to be
                                        rendered, or an iterable with template names
                                        the first one existing will be rendered
        :param context: the variables that should be available in the
                        context of the template.
        """
        context['title'] = self.title
        return render_template(template+".html", **context)


def authentication(parent_method):
    """A decorator to help authentication process"""

    def decorated():
        """The callable decorator"""
        if request.values.get("check"):
            return redirect("/login?next=/" + request.url.replace(request.host_url, ""))
        return parent_method()
    return decorated

