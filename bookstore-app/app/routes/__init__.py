from flask import Blueprint

blueprint = Blueprint('main', __name__)

# Import routes
from .books import *