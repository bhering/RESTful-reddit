#!flask/bin/python
from flask import Flask, jsonify
from info import info

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
