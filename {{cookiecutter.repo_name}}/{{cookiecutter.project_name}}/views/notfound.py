""" 404 view.
"""

from pyramid.view import notfound_view_config


@notfound_view_config(renderer='404.jinja2')
def notfound_view(request):
    """ 404 view.
    """
    request.response.status = 404
    return {}
