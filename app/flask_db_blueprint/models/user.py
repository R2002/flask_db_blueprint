from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100))
