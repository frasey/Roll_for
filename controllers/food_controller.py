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

# SHOW ITEM ADDED
@food_blueprint.route("/food/show", methods=["POST"])
def create_new_item():
    name = request.form["name"]
    category = request.form["category"]

    food = Food(name=name, category=category)
    db.session.add(food)
    db.session.commit()
    return redirect("/food/show")

# SHOW ALL
@food_blueprint.route("/food/show")
def all_food():
    foods = Food.query.all()
    return render_template("/food/show.jinja", foods=foods)

# SHOW ONE ITEM
@food_blueprint.route("/food/<id>")
def show_item(id):
    food = Food.query.get(id)
    return render_template("/food/show_one.jinja", food=food)  

# EDIT - error - URL not found on server
food_blueprint.route("/food/<id>/edit")
def edit_food(id):
    food = Food.query.get(id)
    return render_template("/food/edit.jinja",food=food)

#UPDATE ITEM
@food_blueprint.route("/food/<id>", methods=['POST'])
def update_food(id):
    name = request.form["name"]
    category = request.form["category"]

    food = Food.query.get(id)

    food.name = name
    food.category = category

    db.session.commit()
    return redirect("/food/show")

# DELETE
@food_blueprint.route("/food/<id>/delete", methods=['POST'])
def delete_food(id):
    Food.query.filter_by(id = id).delete
    db.session.commit()
    return redirect("food/show")