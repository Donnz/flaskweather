from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup
import os
import json
import time
import requests
from datetime import datetime

app = Flask(__name__)

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&mode=json&units=metric&appid=6ed285b31705b0f297c8ded67cbdf929"
    response = requests.get(url)
    return response.content

@app.route("/")
def index():
    data = json.loads(get_weather("campinas"))
    return data

@app.route("/json/<city>")
def json_city(city):
    data = json.loads(get_weather(city))
    return data

@app.route("/<city>")
def cities(city):
    data = json.loads(get_weather(city))
    return data

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='192.168.0.2', port=port, debug=False)
