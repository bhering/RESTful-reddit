# RESTful-reddit
An API done as a test, it saves some data from reddit's own API and serves it slightly differently.

### How to kick it off

Pretty standard stuff: get yourself python3, [pip](https://pip.pypa.io/en/stable/) and a [virtual env](https://docs.python.org/3/library/venv.html), activate it and run `$ pip install -r requirements.txt`.

After that you can run `$ source Procfile` to start the debug server, or type in the lines yourself:

```
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
$ flask run
```

I'll let you guess which line to leave out for production.

### Database

For this test, we're using a simple sqlite database that you can initialize (after `$ export FLASK_APP=app.py`) using the command `flask initdb`.

After that, there is a data fetching module aptly named [data_fetcher.py](./data_fetcher.py), that you can run once simply with `$ python data_fetcher.py` or schedule for every day at a specific time (e.g. 14:00) with `$ python data_fetcher.py 14:00`.

A little warning is due: the handling of unexpected parameters is non-existant at this time, and behavior may be unpredictable if you stray from the hour:minute format.

The script has to be running continuously in order for it to work.
