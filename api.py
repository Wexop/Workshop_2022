from flask import Flask, render_template  # pip install flask

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("main.html")


@app.route("/test")
def autre():
    return "dqhsbdhu"


if __name__ == "__main__":
    app.debug = True
    app.run()
