import flask
from flask import Flask, request
import json
server_port = 5000
app = Flask(__name__)

@app.route('/')
def hello_world():

    return ("flask.render_template"
            "")
