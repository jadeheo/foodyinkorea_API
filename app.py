from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbfood

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/seoul')
def city():
   return render_template('Seoul.html')

@app.route('/food')
def food():
   return render_template('food.html')


if __name__ == '__main__':
   app.run('0.0.0.0',port=80,debug=True)