import pandas as pd
import numpy as np
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
    return render_template("index.html", tickers=tickers_)

@app.route("/companies")
def index():
    """companies - Displays the available models"""
    tickers_ = historical.get_tickers()
    return render_template("companies.html")

@app.route("/jupyter")
def jupyter():
    """code - Jupyter Notebook file"""
    return render_template("Stockprer-Tesla.html")

@app.route("/code")
def code():
    """code - Jupyter Notebook file"""
    return render_template("code.html")

@app.route("/models/<ticker>")
def models(ticker):
    """models - It renders Our Jupyter Notebook Wrapper"""
    url = f"http://127.0.0.1:5000/render-models/{ticker}"
    return render_template("models.html", ticker_=url)

@app.route("/render-models/<ticker>")
def render_models(ticker):
    """models - This Function renders a Jupyter Notebook html"""
    return render_template(f"{ticker}.html")

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