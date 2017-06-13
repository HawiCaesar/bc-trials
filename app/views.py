from flask import render_template

from app import app

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/contact-us')
def contact():
	return render_template('contact-us.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/mytasks')
def mytasks():
	return render_template("my-tasks.html")


