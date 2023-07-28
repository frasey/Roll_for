from flask import render_template, redirect, Blueprint, request
from app import db
# Import models

example_blueprint = Blueprint("tasks", __name__)

# Example of showing an individual object
@example_blueprint.route("/example/<id>")
def example_show(id):
    example_obj = Example.query.get(id)
    return render_template("example/show.html", example=example_obj)