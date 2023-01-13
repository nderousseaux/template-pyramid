""" Routes for the {{ cookiecutter.project_name }} application.
"""

def includeme(config):
    """ Add routes to the config.
    """

    config.add_route("home", "/")

    config.scan(".views")
