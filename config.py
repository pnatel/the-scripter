"""Class-based Flask app configuration."""
from os import environ, path

# from dotenv import load_dotenv
from read_env import read_env

basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, ".env"))
read_env()

class Config:
    """Configuration from environment variables."""

    DEBUG = environ.get("DEBUG")
    UPLOAD_FOLDER = environ.get("UPLOAD_FOLDER")
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_ENV = environ.get("FLASK_ENV")
    FLASK_APP = environ.get("FLASK_APP")

    # Flask-Assets
    # LESS_BIN = environ.get("LESS_BIN")
    # ASSETS_DEBUG = True
    # LESS_RUN_IN_DEBUG = True

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG")

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


