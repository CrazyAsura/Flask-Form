import os
from flask import render_template, request, redirect, url_for
from src import app
from src.controler import validate_inputs


@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    validate_inputs()
    
@app.route('/sucess')
def sucess():
    return render_template('sucess.html')

@app.route('/error')
def error():
    e = request.args.get('error')
    return render_template('error.html', error=e)
