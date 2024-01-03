# Roll_for
Using Python, Flask and SQLAlchemy to create a working CRUD app using restful routes. This app is intended to support organisation and disordered eating.

I created an app in which different users can input food preferences, and a random assortment of their options will be generated as a meal plan for a bento-style lunch, along with a shopping list.

Keeping accessibility in mind, the main functionality of this app is on the home page and a darker colour scheme used.


## The Project
This was my first solo project and my first Python project. I had the idea of creating this app before I started the course and was really happy to be able to make it as my first project. I drew on some additional knowledge from having completed a short Introduction to Python course with CodeFirstGirls to import additional modules such as random. I enjoyed styling this app


## What would I do differently or like to keep working on
- As this is an early project, as I learn more I would like to review the code and see where it can be improved.
- As part of our brief, I was making this application as if already signed in. I would like to add authentication so that all users have separate profiles.
- I was quite new to CSS at the time of creating this app and would like to go back over this and tidy up/improve the code in this file.
- I have had some brief training on uploading apps to be hosted on the cloud, and I would quite like to create a version of this app that will work on mobiles and make this available online so that I can use it myself.


## Project screenshots

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

createdb roll_for
flask db init
flask run seed
```

In app.py:
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://<your_postgres_user>@localhost:5432/roll_for"


## To run:
```
flask db upgrade
flask seed
flask run 
```
