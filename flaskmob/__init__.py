"""This is a docstring."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object("config")
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
# csrf = CSRFProtect(app)


from flaskmob import views, api
