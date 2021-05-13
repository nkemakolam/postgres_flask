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
class Product(db.Model):
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

# Create a product route
@app.route('/product',methods=['POST'])

def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    
    new_product = Product(name,description,price,qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Get All Product
@app.route('/product',methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

# Get single Product
@app.route('/product/<id>',methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# update an existing product route
@app.route('/product/<id>',methods=['PUT'])

def update_product(id):
    product = Product.query.get(id)
    # geting the field of the schema
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    
    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return product_schema.jsonify(product)


# Get delete single Product
@app.route('/product/<id>',methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)
#  # add a sample test rout
# @app.route('/', methods=['GET'])
# def get():
#     return jsonify({'msg':'Hello word'})


# Run server
if __name__ ==  '__main__':
    app.run(debug= True)
    #db.create_all()