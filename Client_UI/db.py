from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://postgres:mysecretpassword@localhost/postgres"


db=SQLAlchemy(app)


class Furniture(db.Model):
    __tablename__ = 'furniture'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.VARCHAR(500))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description
    

class Decor(db.Model):
    __tablename__ = 'decor'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.VARCHAR(500))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description

    
class Bedroom(db.Model):
    __tablename__ = 'bedroom'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.VARCHAR(500))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description   


class Bath(db.Model):
    __tablename__ = 'bath'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.VARCHAR(500))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description   


class Art(db.Model):
    __tablename__ = 'art'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.VARCHAR(500))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description

