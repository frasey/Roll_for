from flask import render_template, redirect, Blueprint, request
from app import db
from models.user import User

user_blueprint = Blueprint("user", __name__)

#HOMPAGE WHERE USER CAN GET RANDOM OUTPUT
@user_blueprint.route("/food")
def roll():
    return render_template("index.jinja")

# NEW USER
@user_blueprint.route("/food/new_user")
def add_user():
    users = User.query.all()
    return render_template("user/new.jinja", users=users)

# ADD USER
@user_blueprint.route("/food", methods=["POST"])
def create_new_item():
    name = request.form["name"]

    name = User(name=name)
    db.session.add(name)
    db.session.commit()
    return redirect("/food")