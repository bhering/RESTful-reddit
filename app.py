#!flask/bin/python

# imports here
import click
from   datetime import datetime
from   flask import abort, Flask, g, jsonify, request
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

# this is not the best place to put this
# the function returns based on localtime
def get_timestamp(date,dateformat="%d-%m-%Y"):
	try:
		return datetime.strptime(date,dateformat).timestamp()
	except ValueError:
		abort(400)

@app.route('/posts/', methods=['GET'])
def posts_endpoint():
	db=get_db()
	query='select title, author, ups, num_comments from post '

	constraints=[]
	start_date=request.args.get('start_date')
	end_date=request.args.get('end_date')
	order=request.args.get('order')

	if start_date:
		constraints.append(
			'timestamp > '+str(get_timestamp(start_date)))

	if end_date:
		constraints.append(
			'timestamp < '+str(get_timestamp(end_date)))

	if len(constraints) > 0:
		query+='where '+' and '.join(constraints)

	if order=='ups':
		query+=' order by ups desc'
	elif order=='comments':
		query+=' order by num_comments desc'

	return jsonify([
		{'title':t,'author':a,'ups':u,'comments':c}
		for t,a,u,c in db.execute(query)
	])

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
    app.run()
