""" pshell command for the {{ cookiecutter.project_name }} application.
"""

from . import models

def setup(env):
    """ Setup the environment for the pshell command.
    """

    request = env['request']

    # start a transaction
    request.tm.begin()

    # inject some vars into the shell builtins
    env['tm'] = request.tm
    env['dbsession'] = request.dbsession
    env['models'] = models
