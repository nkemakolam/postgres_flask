from flask import  Flask, jsonify,request
from flask_sqlalchemy import  SQLAlchemy
from flask_marshmallow import  Marshmallow
import  os

#initial app
app = Flask(__name__)

#database  setup

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://nkemakolam:ghosts123@localhost/product_api'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
#initialising db
db = SQLAlchemy(app)
#initialising marshmallow
ma = Marshmallow(app)

#product Class/Model
class Person(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120),unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float) 
    qty = db.Column(db.Integer) 
    # initialise a constructor
    def __init__(self,name,description,price,qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty
# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description','price','qty')

#Initialising schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


#  # add a sample test rout
# @app.route('/', methods=['GET'])
# def get():
#     return jsonify({'msg':'Hello word'})


# Run server
if __name__ ==  '__main__':
    app.run(debug= True)
    #db.create_all()