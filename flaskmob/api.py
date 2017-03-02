from flask import jsonify
from flaskmob import app, db
from flask_restful import Resource, Api

api = Api(app)

class Pokeymon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    color = db.Column(db.String)

    def __init__(self, name, color=None):
        if not color:
            color = "Not Specified"
        self.name = name
        self.color = color

    def __repr__(self):
        return str(self.name)

class PokeymonNapTime(Resource):
    def get(self, name):
        result = Pokeymon.query.filter_by(name=name).first()
        del result.__dict__['_sa_instance_state']
        return jsonify(result.__dict__)

    def post(self, name, color=None):
        new_pokeymon = Pokeymon(name, color)
        db.session.add(new_pokeymon)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return "Success"

api.add_resource(PokeymonNapTime, "/api/1.0/pokeyman/<string:name>")
