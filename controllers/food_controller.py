from flask import render_template, redirect, Blueprint, request
from app import db
from models.user import User
from models.food import Food
import random

food_blueprint = Blueprint("/food", __name__)

# RANDOMISED ITEMS
@food_blueprint.route("/food", methods=["GET"])
def output_random():
    users = User.query.all()
    args = request.args
    user_id = args.get("user")
    if user_id:
        food = Food.query.filter_by(user_id = user_id)
        meal_names = ["main", "fruit", "nuts", "extra nibble", "sweet"]
        meals = []
        for meal_name in meal_names:
            filtered_meals = food.filter_by(category = meal_name).all()
            if len(filtered_meals) >= 1:
                meal = random.choice(filtered_meals)
                meals.append(meal)
        return render_template("index.jinja", user_id=user_id, users=users, meals=meals)
    else:
        return render_template("index.jinja", user_id=user_id, users=users)
    
# NEW
@food_blueprint.route("/food/new")
def add_food():
    users = User.query.all()
    return render_template("food/new.jinja", users=users)

# SHOW ITEM ADDED
@food_blueprint.route("/food/show", methods=["POST"])
def create_new_item():
    user_id = request.form["user_id"]
    name = request.form["name"]
    category = request.form["category"]
    ingredients = request.form["ingredients"]

    food = Food(name=name, category=category, user_id=user_id, ingredients=ingredients)
    db.session.add(food)
    db.session.commit()
    return redirect(f"/users/{ user_id }")

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
    user_id = request.form["user_id"]
    name = request.form["name"]
    category = request.form["category"]
    ingredients = request.form["ingredients"]

    food = Food.query.get(id)

    food.user_id = user_id
    food.name = name
    food.category = category
    food.ingredients = ingredients

    db.session.commit()

    return redirect(f"/users/{ user_id }")

# EDIT
@food_blueprint.route("/food/<id>/edit")
def edit_food(id):
    food = Food.query.get(id)
    user = User.query.all()
    return render_template("food/edit.jinja", food=food, user=user)

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