from flask import Blueprint

generic_sports = Blueprint('sports_api', __name__)

from . import sports_api