import os

DEBUG = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
SQLALCHEMY_TRACK_MODIFICATIONS=False