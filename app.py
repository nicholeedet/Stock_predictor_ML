import json, glob, os
import pandas as pd
import numpy as np
import urllib.request
import historical

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify, render_template
from flask_cors import CORS


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False # Preventing Jsonify to reorder the dictionary elements by the keys
CORS(app)
#################################################
# Flask Routes
#################################################


@app.route("/")
def index():
    """Index - Landing Page"""
    tickers_ = historical.get_tickers()
    return render_template("base.html", tickers=tickers_)

#################################################
# API generators                               #
###############################################

@app.route("/list_tickers")
def list_tickers():
    """Returns a list with Ticker names and their symbols"""
    return jsonify(historical.get_tickers())

@app.route("/get_historical/<ticker>")
def get_historical(ticker):
    """Returns a list with historical data in JSON format"""
    result = historical.get_historical(ticker)
    return jsonify(result)



if __name__ == "__main__":
    app.run()