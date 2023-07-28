from flask import render_template, redirect, Blueprint, request
from app import db
from models.user import User
from models.food import Food

food_blueprint = Blueprint("/food", __name__)

# Example of showing an individual object
# @example_blueprint.route("/example/<id>")
# def example_show(id):
#     example_obj = Example.query.get(id)
#     return render_template("example/show.html", example=example_obj)

# NEW
@food_blueprint.route("/food/new")
def add_food():
    users = User.query.all()
    return render_template("food/new.jinja", users=users)

@food_blueprint.route("/food/show", methods=["POST"])
def create_new_item():
    name = request.form["name"]
    category = request.form["category"]

    food = Food(name=name, category=category)
    db.session.add(food)
    db.session.commit()
    return redirect("/food/show")

@food_blueprint.route("/food/show")
def all_food():
    foods = Food.query.all()
    return render_template("/food/show.jinja", foods=foods)