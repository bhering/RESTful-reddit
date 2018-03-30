#!flask/bin/python
import click
from flask import Flask, jsonify
from info import info

app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False

@app.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')

@app.route('/')
def index():
    return jsonify(info)

@app.errorhandler(404)
def page_not_found(error):
	return jsonify(
	{
		'error':'this end point is not yet implemented',
		'code':404
	})

if __name__ == '__main__':
    app.run(debug=True)
