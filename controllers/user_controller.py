from flask import render_template, redirect, Blueprint, request
from app import db
from models.user import User

user_blueprint = Blueprint("user", __name__)

# Example of showing an individual object
# @example_blueprint.route("/example/<id>")
# def example_show(id):
#     example_obj = Example.query.get(id)
#     return render_template("example/show.html", example=example_obj)

@user_blueprint.route("/food")
def roll():
    return render_template("index.jinja")