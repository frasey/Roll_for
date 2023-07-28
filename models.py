from app import db

# Example Model
# ------------------------------------------------
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    food = db.relationship("Food", backref="user")

    def __repr__(self):
        return f"<Name: {self.name}>"
    

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String(64))
    user = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"<Food: {self.name}, {self.type}>"
