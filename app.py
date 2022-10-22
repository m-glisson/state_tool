from flask import Flask, render_template, jsonify, request, redirect, url_for 
from data_source import DataSource 

app = Flask(__name__)
source_data = DataSource()


@app.route('/')
def index():
    return 'This is the home page'


@app.route('/thread', methods=['GET'])
def thread():
    return jsonify(source_data.get_value())