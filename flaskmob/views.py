from flaskmob import app

@app.route("/")
def index():
    return "Hello OPUG for the sake of being programmers!"