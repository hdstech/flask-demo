from flaskmob import app, db
from flaskmob.forms import PokeyForm
from flask import render_template, redirect, request
from flaskmob.api import addNewPokeymon, getPokeymonList

@app.route("/")
def index():
    pokeymon = getPokeymonList()
    return render_template('index.html', pokeymon=pokeymon)

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = PokeyForm()
    if form.validate_on_submit():
        return addNewPokeymon(form.name.data, form.color.data)
    return render_template('pokeymonForm.html', form=form)
