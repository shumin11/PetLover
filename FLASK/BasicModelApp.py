import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> basicModelApp.py 

app = Flask(__name__)
# tell the database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite') # This is the path to our database file.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just to supress a warning from SQLAlchemy as it will soon be removed

db = SQLAlchemy(app)

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."
    

