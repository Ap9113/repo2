import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Change this in production
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key_change_me!')

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
