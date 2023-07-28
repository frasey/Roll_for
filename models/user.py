from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    food = db.relationship("Food", backref="user")

    def __repr__(self):
        return f"<Name: {self.name}>"