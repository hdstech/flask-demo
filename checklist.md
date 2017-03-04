Tutorial: [http://codehandbook.org/flask-restful-api-using-python-mysql/](http://codehandbook.org/flask-restful-api-using-python-mysql/)

Setup Python
* [ ] Install `Python`
* [ ] Install `pip`
* [ ] Pip install `flask-restful`
* [ ] Pip install `flask-mysql`

Setup our API
* [ ] Create a new directory
* [ ] Make a file `api.py`
* [ ] Import `Flask` from `flask`
* [ ] Import `Resource`, `Api`, `reqparse` from `flask_restful`
* [ ] Import `MySQL` from `flask.ext.mysql`
* [ ] Set `app` equal to `Flask(__name__)`
* [ ] Set `api` equal to `Api(app)`
* [ ] Set `mysql` equal to `MySQL`
* [ ] Add a conditional for when `__name__` equals `__main__`
* [ ] In the body of the conditional call `app.run(debug=True)`

Code our first endpoint `CreateUser`
* [ ] add a `CreateUser` class which takes in `Resource` as an argument
* [ ] add a `Post` method which takes `self` as an argument
* [ ] return a dictionary with key of `status` and value of `success` as the body of the `Post` method. (This is for testing purposes.)
* [ ] Add `CreateUser` as a resource with an endpoint of `/CreateUser` via the `api.add_resource` method

Start the server and check our `CreateUser` endpoint works
* [ ] Export our app in the shell with `export FLASK=api.py`
* [ ] Run the server in the shell with `flask run`
* [ ] Use Postman to make a post request to `localhost:5000/CreateUser` setting values for `email` and `password` query params

Setup MySQL database
* [ ] use `app.config` to set parameters for the database: `MYSQL_DATABASE_USER`, `MYSQL_DATABASE_PASSWORD`, `MYSQL_DATABASE_DB`, `MYSQL_DATABASE_HOST`
* [ ] initialize the database with `mysql.init_app(app)`
* [ ] Within our endpoint call, start a MySQL connection
* [ ] Create a cursor to interact with the database
