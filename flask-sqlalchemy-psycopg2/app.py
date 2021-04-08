from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://nkemakolam:ghosts123@localhost/easymigrate'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstName = db.Column(db.String(120),unique=False)
    lastName = db.Column(db.String(120),unique=False)
    email = db.Column(db.String(120),unique=False) 

    def __init__(self,firstName,lastName,email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
if __name__ == '__main__':
    db.create_all()
