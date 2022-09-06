from flask import Flask, render_template, request  # pip install flask
from script import fakeNewsAnalyser
from script.fakeNewsAnalyser import fakeNewsAnalyse

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    url = request.args.get("url")
    return fakeNewsAnalyse(url)


@app.route("/test")
def autre():
    return "dqhsbdhu"


if __name__ == "__main__":
    app.debug = True
    app.run()
