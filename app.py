from flask import Flask, request
from flask_bcrypt import Bcrypt
from db import get_db

app = Flask(__name__)
bcrypt = Bcrypt(app)
db = get_db()

from bson.objectid import ObjectId

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Online Store API!', 200

# users collection operationss
@app.route('/register', methods=['POST'])
def register():
    user = {
        "_id": ObjectId(),
        "username": request.json['username'],
        "password": bcrypt.generate_password_hash(request.json['password']),
        "is_active": True,
        "role": "client"
    }
    db.users.insert_one(user)
    return 'User registered', 201

@app.route('/login', methods=['POST'])
def login():
    user = db.users.find_one({"username": request.json['username']})
    if user and bcrypt.check_password_hash(user['password'], request.json['password']):
        return 'Logged in', 200
    return 'Invalid credentials', 401

# categories collection operations
@app.route('/categories', methods=['POST'])
def create_category():
    category = {
        "_id": ObjectId(),
        "name": request.json['name']
    }
    db.categories.insert_one(category)
    return 'Category created', 201

@app.route('/categories/<id>', methods=['PUT'])
def update_category(id):
    db.categories.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"name": request.json['name']}}
    )
    return 'Category updated', 200

@app.route('/categories/<id>', methods=['DELETE'])
def delete_category(id):
    db.categories.delete_one({"_id": ObjectId(id)})
    return 'Category deleted', 200

# products collection operations
@app.route('/products', methods=['POST'])
def create_product():
    product = {
        "_id": ObjectId(),
        "name": request.json['name'],
        "amount_in_stock": request.json['amount_in_stock'],
        "price": request.json['price'],
        "in_stock": True
    }
    db.products.insert_one(product)
    return 'Product created', 201

@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    db.products.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "name": request.json['name'],
            "amount_in_stock": request.json['amount_in_stock'],
            "price": request.json['price']
        }}
    )
    return 'Product updated', 200

@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    db.products.delete_one({"_id": ObjectId(id)})
    return 'Product deleted', 200

if __name__ == '__main__':
    app.run(debug=True)
