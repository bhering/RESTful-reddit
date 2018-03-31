#!flask/bin/python

# imports here
import click
from   datetime import datetime
from   flask import Flask, g, jsonify, request
from   info import info
import os
import sqlite3


### app instantiation ###

app = Flask(__name__)
app.config.update({
	'JSON_SORT_KEYS':False,
	'DATABASE':os.path.join(app.root_path, 'posts.db'),
})

### cli commands ###

@app.cli.command('initdb')
def init_db():
	db = get_db()
	with app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()
	click.echo('db started')


### database stuff ###

def connect_db():
	r=sqlite3.connect(app.config['DATABASE'])
	r.row_factory=sqlite3.Row
	return r


def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db=connect_db()
		return g.sqlite_db

### routing ###

@app.route('/')
def index():
    return jsonify(info)

@app.route('/posts/', methods=['GET'])
def posts_endpoint():
	db=get_db()
	query='select title, author from posts '
	if request.args.get('start_date'):
		st=datetime.strptime(
		request.args.get('start_date'),
		"%d-%m-%Y").timestamp()
		return jsonify({'result':st})
	else:
		return jsonify(request.values)

### error handling ###

@app.errorhandler(404)
def page_not_found(error):
	return jsonify(
	{
		'error':'this end point is not yet implemented',
		'code':error.code,
	})


@app.errorhandler(400)
def bad_request(error):
	return jsonify(
	{
		'error':'double check the query parameters',
		'code':error.code,
	})

### teardown ###

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


### just in case ###

if __name__ == '__main__':
    app.run(debug=True)
