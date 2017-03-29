from flaskmob import app
from flaskmob.forms import PokeyForm
from flask import render_template

@app.route("/")
def index():
    return "Hello OPUG for the sake of being programmers!"

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = PokeyForm()
    if form.validate_on_submit():
        return redirect(f'/api/1.0/pokeyman/{form.name}')
    return render_template('pokeymonForm.html', form=form)
