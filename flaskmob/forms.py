from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class PokeyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
