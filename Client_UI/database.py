from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, MetaData
#from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

""" engine = create_engine("postgresql+psycopg2://postgres:password@localhost/inspire")
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import app.models
    Base.metadata.create_all(bind=engine) """

""" engine_URL = URL("postgresql", username="postgres", password="password", host="localhost", database="inspire")
engine = create_engine(engine_URL)
Base = declarative_base()
Base.metadata.reflect(engine) """

def table_to_declarative(uri):
    """ Reflects all tables to declarative """

    Base = declarative_base()
    engine = create_engine(uri)
    metadata = MetaData(bind=engine)
    Base.metadata = metadata

    g = globals()

    metadata.reflect()

    for tablename, tableobj in metadata.tables.items():
        g[tablename] = type(str(tablename), (Base,), {'__table__': tableobj })
        print("reflecting {0}".format(tablename))

    Session = sessionmaker(bind=engine)
    return Session()

CONNECTION_URI = "postgresql://postgres:password@localhost/inspire"














""" 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

""" import sys
sys.path.insert(0,"..")
from Admin.app import db, Furniture """

app = Flask(__name__)

""" db.app = apps
db.init_app = apps """

app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://postgres:password@localhost/inspire"
""" db=SQLAlchemy(app)
db.Model.metadata.reflect(db.engine) """

engine_URL = URL("postgresql", username="postgres", password="password", host="localhost", database="inspire")
engine = create_engine(engine_URL)
Base = declarative_base()
Base.metadata.reflect(engine)

@app.route("/")
def index():
    return render_template("index.html")

""" @app.route("/home")
def home():
    furnitures = Furniture.query.all()
    return render_template("home.html", furnitures=furnitures) """


""" class Furniture(db.Model):
    __table__ = db.Model.metadata.tables["FURNITURE"]
    
    def __repr__(self) -> str:
        return self.name, self.link, self.description """





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug="TRUE")
    #app.run(host="0.0.0.0", port=80)
 """