""" rate api """

from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home() -> Response:
    """ home """
    return "<h1>Hello, World!</h1>"



app.run()