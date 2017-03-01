from flaskmob import app, db
from flask_restful import Resource, Api

class Pokeymon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    color = db.Column(db.String)


