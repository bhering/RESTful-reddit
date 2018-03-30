# RESTful-reddit
An API done as a test, it saves some data from reddit's own API and serves it slightly differently.

### How to kick it off

Pretty standard stuff: get yourself [pip](https://pip.pypa.io/en/stable/) and a [virtual env](https://docs.python.org/3/library/venv.html), activate it and run `$ pip install -r requirements.txt`.

After that you can run the commands in the Procfile to start the debug server:

```
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
$ flask run
```

I'll let you guess which line to leave out for production.
