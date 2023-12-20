from flask import render_template, redirect, Blueprint, request
from app import db
from models.user import User
from models.food import Food

user_blueprint = Blueprint("user", __name__)

# NEW USER
@user_blueprint.route("/food/new_user")
def add_user():
    users = User.query.all()
    return render_template("user/new.jinja", users=users)

# ADD USER
@user_blueprint.route("/food", methods=["POST"])
def create_new_user():
    name = request.form["name"]

    name = User(name=name)
    db.session.add(name)
    db.session.commit()
    return redirect("/food")

# SHOW USER FOODS
@user_blueprint.route("/users/<id>")
def all_user_food(id):
    user = User.query.get(id)
    foods = Food.query.filter_by(user_id = id)
    return render_template("/user/all_food.jinja", user=user, foods=foods)

# UPDATE USER
@user_blueprint.route("/users/<id>", methods=["POST"])
def update_user(id):
    name = request.form["name"]

    user = User.query.get(id)

    user.user_id = id
    user.name = name
    db.session.commit()
    return redirect("/food")

# LIST OF USERS
@user_blueprint.route("/users/all")
def users():
    users = User.query.all()
    return render_template("user/list.jinja", users=users)

# EDIT
@user_blueprint.route("/users/<id>/edit")
def edit_user(id):
    user = User.query.get(id)
    return render_template("user/edit.jinja", user=user)

# DELETE USER
@user_blueprint.route("/users/<id>/delete")
def check(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/food")