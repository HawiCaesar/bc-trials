from flask import render_template

from app import app

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")




"""
@app.route('/gh')
def gh():
	return render_template("a")

fewnfewfrenf()
"""


