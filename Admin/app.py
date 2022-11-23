from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:password@localhost/inspire'

db=SQLAlchemy(app)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/add-furniture")
def addFurniture():
    return render_template("add-furniture.html")

@app.route("/submit-furniture", methods=["POST"])
def submit():
    name = request.form['name']
    link = request.form['link']
    description = request.form['description']

    furniture = Furniture(name=name, link=link, description=description)
    db.session.add(furniture)
    db.session.commit()

    return render_template("dashboard.html")

@app.route("/furniture")
def furniture():
    return render_template("furniture.html")

@app.route("/bedding")
def bedding():
    return render_template("bedding.html")

@app.route("/decor")
def decor():
    return render_template("decor.html")

@app.route("/bath")
def bath():
    return render_template("bath.html")

@app.route("/art")
def art():
    return render_template("art.html")

@app.route("/about-us")
def about():
    return render_template("about-us.html")




class Furniture(db.Model):
    __tablename__ = 'furniture'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug="TRUE")