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



""" @app.route("/edit-furniture/<int:id>", methods=["GET", "POST"])
def editFurniture(id):
    item = Furniture.query.get_or_404(id)
    if request.method == "POST":
        #name = request.form["name"] or
        item.name = request.form["name"]
        item.link = request.form["link"]
        item.description = request.form["description"]

        try:
            db.session.commit()
            flash("Furniture detail updated successfully!")
            
            return render_template("furniture.html", item=item)
        except:
            flash("Error updating furniture details!")
            return render_template("edit-furniture.html", item=item)
    else:
        render_template("furniture.html", item=item) """


@app.route("/add-furniture")
def addFurniture():
    return render_template("add-furniture.html")

@app.route("/add-furniture", methods=["POST"])
def submitFurniture():
    name = request.form['name']
    link = request.form['link']
    description = request.form['description']

    furniture = Furniture(name=name, link=link, description=description)
    db.session.add(furniture)
    db.session.commit()

    return render_template("furniture.html")

@app.route("/furniture")
def furniture():
    furnitures = Furniture.query.all()
    return render_template("furniture.html", furnitures=furnitures)

@app.route("/delete-furniture/<int:id>")
def deleteFurniture(id):
    item = Furniture.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        flash("Furniture detail deleted successfully!")
        furnitures = Furniture.query()
        return render_template("furniture.html", furnitures=furnitures)
    except:
        flash("Error delete furniture detail!")
        return render_template("furniture.html", item=item)



@app.route("/add-decor")
def addDecor():
    return render_template("add-decor.html")

@app.route("/add-decor", methods=["POST"])
def submitDecor():
    name = request.form['name']
    link = request.form['link']
    description = request.form['description']

    decor = Decor(name=name, link=link, description=description)
    db.session.add(decor)
    db.session.commit()

    return render_template("decor.html")

@app.route("/decor")
def decor():
    decors = Decor.query.all()
    return render_template("decor.html", decors=decors)

@app.route("/delete-decor/<int:id>")
def deleteDecor(id):
    item = Decor.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        flash("Decor detail deleted successfully!")
        decors = Decor.query()
        return render_template("decor.html", decors=decors)
    except:
        flash("Error delete decor detail!")
        return render_template("decor.html", item=item)



@app.route("/add-bedroom")
def addBedroom():
    return render_template("add-bedroom.html")

@app.route("/add-bedroom", methods=["POST"])
def submitBedroom():
    name = request.form['name']
    link = request.form['link']
    description = request.form['description']

    bedroom = Bedroom(name=name, link=link, description=description)
    db.session.add(bedroom)
    db.session.commit()

    return render_template("bedroom.html")

@app.route("/bedroom")
def bedroom():
    bedrooms = Bedroom.query.all()
    return render_template("bedroom.html", bedrooms=bedrooms)

@app.route("/delete-bedroom/<int:id>")
def deleteBedroom(id):
    item = Bedroom.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        flash("Bedroom detail deleted successfully!")
        bedrooms = Bedroom.query()
        return render_template("bedroom.html", bedrooms=bedrooms)
    except:
        flash("Error delete bedroom detail!")
        return render_template("bedroom.html", item=item)



@app.route("/add-bath")
def addBath():
    return render_template("add-bath.html")

@app.route("/add-bath", methods=["POST"])
def submitBath():
    name = request.form['name']
    link = request.form['link']
    description = request.form['description']

    bath = Bath(name=name, link=link, description=description)
    db.session.add(bath)
    db.session.commit()

    return render_template("bath.html")

@app.route("/bath")
def bath():
    baths = Bath.query.all()
    return render_template("bath.html", baths=baths)

@app.route("/delete-bath/<int:id>")
def deleteBath(id):
    item = Bath.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        flash("Bath detail deleted successfully!")
        baths = Bath.query()
        return render_template("bath.html", baths=baths)
    except:
        flash("Error delete bath detail!")
        return render_template("bath.html", item=item)





@app.route("/add-art")
def addArt():
    return render_template("add-art.html")

@app.route("/add-art", methods=["POST"])
def submitArt():
    name = request.form['name']
    link = request.form['link']
    description = request.form['description']

    art = Art(name=name, link=link, description=description)
    db.session.add(art)
    db.session.commit()

    return render_template("art.html")

@app.route("/art")
def art():
    arts = Art.query.all()
    return render_template("art.html", arts=arts)

@app.route("/delete-art/<int:id>")
def deleteArt(id):
    item = Art.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        flash("Art detail deleted successfully!")
        arts = Art.query()
        return render_template("art.html", arts=arts)
    except:
        flash("Error delete art detail!")
        return render_template("art.html", item=item)





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