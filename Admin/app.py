from flask import Flask, render_template, request, session, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user

app = Flask(__name__)

app.config["SECRET_KEY"] = "!£$%^&*()LKJHGFDSrtyA}:@<>?"

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:password@localhost/inspire'

db=SQLAlchemy(app)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def registered():
    session['secret']='sec'
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    user = Profile.query.filter_by(email=email).first() 
    if user:
        flash('Email address already exists in the database!', category="error")
        return redirect(url_for('register'))
    
    if password1 != password2:
        flash('Both passwords do not match! Try registering again.', category='error')
        return redirect(url_for('register'))
    else:
        new_profile = Profile(name=name, phone=phone, email=email, password=generate_password_hash(password1, method='sha256'))
        db.session.add(new_profile)
        db.session.commit()
        flash('Account created. Please login with email and passsword', category='success')
        return redirect(url_for('dashboard'))

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/furniture")
def addFurniture():
    return render_template("add-furniture.html")

@app.route("/furniture", methods=["POST"])
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
    

class Decor(db.Model):
    __tablename__ = 'decor'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description

    
class Bedroom(db.Model):
    __tablename__ = 'bedroom'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description   


class Bath(db.Model):
    __tablename__ = 'bath'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description   


class Art(db.Model):
    __tablename__ = 'art'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description


class About(db.Model):
    __tablename__ = 'about'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __init__(self, name, link, description):
        self.name = name
        self.link= link
        self.description = description


class Profile(UserMixin, db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    phone = db.Column(db.String(40))
    email = db.Column(db.String(40))
    password = db.Column(db.String(255))

    def __init__(self, name, phone, email, password):
        self.name = name
        self.phone= phone
        self.email = email
        self.password = password




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug="TRUE")