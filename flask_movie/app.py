from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nkemakolam:ghosts123@localhost/slidshop'
db = SQLAlchemy(app)

class User(db.Model):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email=email
    def __repr__(self):
        return '<User %r>' % self.username



@app.route('/')
def index():
    return "<h1 style='coloer:blue'> Hello World</h1>"

if __name__ == "__main__":
    app.run()
