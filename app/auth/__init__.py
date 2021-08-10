# inside authentication package

from flask import Blueprint

authentication = Blueprint('authentication', __name__, template_folder='templates')

# this package route import
from app.auth import routes

