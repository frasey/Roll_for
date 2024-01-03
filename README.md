# Roll_for
Using Python, Flask and SQLAlchemy to create a working CRUD app using restful routes. This app is intended to support organisation and disordered eating. 

I created an app in which different users can input food preferences, and a random assortment of their options will be generated as a meal plan for a bento-style lunch, along with a shopping list.

The title of this project is 'Roll_For [lunch]'. I focused on lunch as a meal that I always struggle to organise for, but the idea is that the app could be used for any and all meal planning that someone may find difficult. 

Keeping accessibility in mind, the main functionality of this app is on the home page and a darker colour scheme used.


## The Project
This was my first solo project and my first Python project. I had the idea of creating this app before I started the course and was really happy to be able to make it as my first project. I drew on some additional knowledge from having completed a short Introduction to Python course with CodeFirstGirls to import additional modules such as random. I enjoyed styling this app


## What would I do differently or like to keep working on
- As this is an early project, as I learn more I would like to review the code and see where it can be improved.
- As part of our brief, I was making this application as if already signed in. I would like to add authentication so that all users have separate profiles.
- I was quite new to CSS at the time of creating this app and would like to go back over this and tidy up/improve the code in this file.
- I have had some brief training on uploading apps to be hosted on the cloud, and I would quite like to create a version of this app that will work on mobiles and make this available online so that I can use it myself.


## Project screenshots

|          |           |           |
| -------- | --------- | --------- |
| <img width="340" alt="Homepage (no user)" src="https://github.com/frasey/Roll_for/assets/129194569/aca500e1-f0d5-417c-b43c-fd2f4ae86f52"> |
 <img width="340" alt="Homepage (user)" src="https://github.com/frasey/Roll_for/assets/129194569/cc412034-782c-487d-ba71-4e43f0b897f7">
| <img width="340" alt="User roll" src="https://github.com/frasey/Roll_for/assets/129194569/1e88e6bb-340b-407a-a09f-2392cebcd930"> |
| Homepage (no user) | Homepage with user | User roll |
| <img width="340" alt="User food list" src="https://github.com/frasey/Roll_for/assets/129194569/402a88d7-c44d-441c-b2a1-0b2f7308a466"> | <img width="340" alt="Add food" src="https://github.com/frasey/Roll_for/assets/129194569/2d1c191d-598e-468d-94b5-21353a496f87">
| <img width="340" alt="Edit-delete food" src="https://github.com/frasey/Roll_for/assets/129194569/f57badf8-2b67-459d-adbd-1493f7d6e951"> |
| User food list | Add food | Edit/delete food |
| <img width="340" alt="Current users" src="https://github.com/frasey/Roll_for/assets/129194569/adccda13-2524-4403-a484-6373bcdb698e"> | <img width="340" alt="New user" src="https://github.com/frasey/Roll_for/assets/129194569/b7c9aa5c-b626-4f73-a557-497618cc644a"> | <img width="340" alt="Update - delete user" src="https://github.com/frasey/Roll_for/assets/129194569/dce00f0b-38c8-4f32-b34c-110942ed1306"> |
| Current users | New user | Edit/delete user |


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
