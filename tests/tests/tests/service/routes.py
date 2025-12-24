from flask import Flask, jsonify, request
from service.models import Product, db

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def list_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])
