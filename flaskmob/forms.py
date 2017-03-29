from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class PokeyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    color = SelectField(u'color', choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), ('bgum', 'BubbleGum')])