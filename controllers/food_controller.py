from flask import render_template, redirect, Blueprint, request
from app import db
from models.user import User

food_blueprint = Blueprint("/food", __name__)

# Example of showing an individual object
# @example_blueprint.route("/example/<id>")
# def example_show(id):
#     example_obj = Example.query.get(id)
#     return render_template("example/show.html", example=example_obj)

# NEW
@food_blueprint.route("/food/new", methods=["POST"])
def add_food():
    users = User.query.all()
    return render_template("food/new.jinja", users=users)

@foo