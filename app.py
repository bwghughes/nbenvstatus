""" Simple App to show environment status """
import os
from apistar import Command
from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp as App

from project.commands import create_envs, create_env
from project.models import Base
from project.routes import ROUTES

SETTINGS = {
    'TEMPLATES': {
        'ROOT_DIR': 'templates',     # Include the 'templates/' directory.
        'PACKAGE_DIRS': ['apistar']  # Include the built-in apistar templates.
    },
    "DATABASE": {
        "URL": os.getenv("ENVSTATUS_DB_URL"),
        "METADATA": Base.metadata
    }
}

app = App(routes=ROUTES, 
          settings=SETTINGS,
          commands=sqlalchemy_backend.commands + [Command('create_envs', create_envs),
                    Command('create_env', create_env)],
          components=sqlalchemy_backend.components)
