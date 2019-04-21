import os
from flask import Blueprint

api = Blueprint("api", __name__,
                static_folder="static")

base_dir = os.path.abspath(os.path.dirname(__file__))

from .encoding import routes
from .encryption import routes
