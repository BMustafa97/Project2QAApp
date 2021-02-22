from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from application import routes
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///testdb.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Generator(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    result = db.Column(db.String(50), nullable=True)
db.drop_all()
db.create_all()

@app.route("/", methods=['GET'])
def home():
    product = requests.get("http://localhost:5003/product")
    result = product.text
    products = result
#    db.session.add(result)
#    db.session.commit()
    return render_template("home.html", product=result, products=products)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)