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

A little warning is due: the handling of unexpected parameters is non-existant at this time, and behavior may be unpredictable if you stray from the `HH:MM` format.

The script has to be running continuously in order for it to work.

### Usage

By default, the server will be running on `http://localhost:8000`. The API has two endpoints currently:
- `/posts` with the GET query parameters `start_date=DD-MM-YYYY`, `end_date=DD-MM-YYYY` and `order=<order>` - which can be `ups` or `comments`
- `/authors` with the single GET parameter `order=<order>` - which can also be `ups` or `comments`

All parameters are optional.

Examples: `http://localhost:5000/posts/?start_date=01-01-2018&end_date=31-03-2018&order=ups` and `http://localhost:5000/authors/?order=comments`

### Future Work

Generalizing which subreddits to sample from, and also swtiching from using the sqlite3 library to SQLAlchemy so it can be plugged into any type of DB.

Also, obviously, this needs to be split into more files than the monolytic app.py, eventually.

### tl;dr

With python at least version 3.6, and virtualenv installed...

```
$ git clone https://github.com/bhering/RESTful-reddit.git
$ cd RESTFUL-reddit
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ flask initdb
$ python data_fetcher.py
$ export FLASK_APP=app.py
$ flask run
```

And then try accessing in your browser:

`http://localhost:5000/posts/?start_date=01-01-2018&end_date=31-03-2018&order=ups` 
`http://localhost:5000/authors/?order=comments`
