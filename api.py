import flask
from flask import Flask, render_template, request  # pip install flask
from script import fakeNewsAnalyser
from script.fakeNewsAnalyser import fakeNewsAnalyse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def hello():
    url = request.args.get("url")
    response = flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return fakeNewsAnalyse(url)


@app.route("/test")
def autre():
    return "dqhsbdhu"


if __name__ == "__main__":
    app.debug = True
    app.run()
