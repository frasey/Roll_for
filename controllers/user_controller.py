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
def create_new_item():
    name = request.form["name"]

    name = User(name=name)
    db.session.add(name)
    db.session.commit()
    return redirect("/food")

# RANDOM FOOD
# @user_blueprint.route("/food/<user.id>/list")
# def output_random():
#     main = random.choice(Food.query.filter_by(category = "main").all())
#     print(main)
#     fruit = random.choice(Food.query.filter_by(category = "fruit").all())
#     print(fruit)
#     nuts = random.choice(Food.query.filter_by(category = "nuts").all())
#     print(nuts)
#     nibble = random.choice(Food.query.filter_by(category = "extra nibble").all())
#     print(nibble)
#     sweet = random.choice(Food.query.filter_by(category = "sweet").all())
#     print(sweet)
#     return render_template("user/list.jinja", main=main,  fruit=fruit, nuts=nuts, nibble=nibble, sweet=sweet)

# SHOW USER FOODS
@user_blueprint.route("/users/<id>")
def all_user_food(id):
    user = User.query.get(id)
    foods = Food.query.all()
    return render_template("/user/all_food.jinja", user=user, foods=foods)