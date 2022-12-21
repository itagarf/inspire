import os
import sys
#sys.path.insert(0,"..")
from flask import Flask, render_template
#from Admin.app import db, Furniture, Decor, Bedroom, Bath, Art
from db import db, Furniture, Decor, Bedroom, Bath, Art


app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
#app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://postgres:mysecretpassword@localhost/postgres"
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://postgres:password@localhost/inspire"

db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    #db.create_all()
    furnitures = Furniture.query.all()
    decors = Decor.query.all()
    bedrooms = Bedroom.query.all()
    baths = Bath.query.all()
    arts = Art.query.all()
    return render_template("home.html", furnitures=furnitures, decors=decors, bedrooms=bedrooms, baths=baths, arts=arts)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug="TRUE")
#    #app.run(host="0.0.0.0", port=80)