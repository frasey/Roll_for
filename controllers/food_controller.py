from flask import render_template, redirect, Blueprint, request
from app import db
from models.user import User
from models.food import Food
from sqlalchemy.sql.expression import func
import random

food_blueprint = Blueprint("/food", __name__)

# RANDOMISED ITEMS
@food_blueprint.route("/food")
def output_random():
    main = random.choice(Food.query.filter_by(category = "main").all())
    print(main)
    fruit = random.choice(Food.query.filter_by(category = "fruit").all())
    print(fruit)
    nuts = random.choice(Food.query.filter_by(category = "nuts").all())
    print(nuts)
    nibble = random.choice(Food.query.filter_by(category = "extra nibble").all())
    print(nibble)
    sweet = random.choice(Food.query.filter_by(category = "sweet").all())
    print(sweet)
    return render_template("index.jinja", main=main,  fruit=fruit, nuts=nuts, nibble=nibble, sweet=sweet)

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

# EDIT
@food_blueprint.route("/food/<id>/edit")
def edit_food(id):
    food = Food.query.get(id)
    return render_template("food/edit.jinja", food=food)

# DELETE
@food_blueprint.route("/food/<id>/delete")
def check(id):
    food = Food.query.get(id)
    db.session.delete(food)
    db.session.commit()
    return redirect("/food/show")

# INFO PAGE
@food_blueprint.route("/food/tips")
def tips():
    return render_template("/food/tips.jinja")