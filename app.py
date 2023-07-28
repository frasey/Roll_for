from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import all models


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://eileinfraser@localhost:5432/roll_for"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and Register Controllers
from models import User, Food

@app.route("/")
def home():
    return render_template("index.html", title="Hello World")
