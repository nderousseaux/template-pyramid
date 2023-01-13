""" Entry point for the application.
"""

from os import getenv
from pyramid.config import Configurator
from pyramid.renderers import JSON

def main(global_config, **settings): # pylint: disable=unused-argument
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include("pyramid_tm")

    #JSON Renderer
    json_renderer = JSON()
    config.add_renderer("json", json_renderer)

    #Routes
    config.include("cornice")
    config.include('.routes')
    config.scan()

    app = config.make_wsgi_app()

    return app
