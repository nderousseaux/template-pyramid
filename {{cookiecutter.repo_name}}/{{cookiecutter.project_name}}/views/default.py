""" Default views for the {{ cookiecutter.project_name }} application.
"""

from pyramid.view import view_config

@view_config(route_name="home", renderer="json")
def my_view(request): # pylint: disable=unused-argument
    """ Default view.
    """

    return {"project": "{{ cookiecutter.project_name }}"}
