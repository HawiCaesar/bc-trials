from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from app import views

app.config.from_object('config')


"""
We can Model how the data should look like, 
for example a user class to represent users 
or an items class for Bucket list items, 
Have a View(HTML/CSS) for the data and have
 Controller logic for how users may interact
  with the data eg CRUD(create, read, update,
   delete) operations

"""

