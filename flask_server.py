#!/usr/bin/python3
from flask import Flask, request
import json
import grammar
import gluply
from oracle import Oracle

# To run: FLASK_APP=server.py python3 -m flask run --host=0.0.0.0
app = Flask(__name__)

@app.route("/")
def hello():
    param = request.args.get('request')
    parsed_input = gluply.read_input(param)
    chatbot = Oracle()
    return chatbot.ask(parsed_input)
