#    app/catalog/__init__.py

from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')

from app.catalog import routes  # watch videos 35 for avoid circular reference problem we write it in bottom

