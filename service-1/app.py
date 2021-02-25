from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from application import routes
import os
from os import getenv
import mysql.connector

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/flaskdb"
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Generator(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    result = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"{self.id} | {self.result}"
db.drop_all()
db.create_all()

@app.route("/home", methods=['GET'])
def home():
    product = requests.get("http://34.105.75.14:5003/product")
    result = product.text
    results = Generator(result=result)
    db.session.add(results)
    db.session.commit()
    products = Generator.query.all()
 #   products.execute("SELECT * FROM Generator LIMIT 5 OFFSET 2")
  #  limit = Generator.query.order_by(Generator.id.desc()).limit(5)
    return render_template("home.html", product=result, products=products)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)