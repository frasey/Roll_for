# Roll_for
Using Python, Flask and SQLAlchemy to create a working CRUD app using restful routes. This app is intended to support organisation and disordered eating.

I created an app in which different users can input food preferences, and a random assortment of their options will be generated as a meal plan for a bento-style lunch, along with a shopping list.

Keeping accessibility in mind, the main functionality of this app is on the home page and a darker colour scheme used.

## Dependencies:
```
Python 3,
PostgreSQL
```

## Start guide:
```
pip 3 install flask
pip3 install flask-sqlalchemy
pip3 install python-dotenv
pip3 install flask-migrate
pip3 install psychopg2

createdb workout
flask db init
flask run seed
```

In app.py:
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://<your_postgres_user>@localhost:5432/workout"


## To run:
```
flask db upgrade
flask seed
flask run 
```
