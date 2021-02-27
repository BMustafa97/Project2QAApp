from flask import Flask, Response, request
import random
import requests
import os
from os import getenv

app = Flask(__name__)
@app.route('/product',methods=['GET'])
def product():
    firstname = requests.get("http://34.105.121.250:5001/firstname")
    slogan = requests.get("http://34.105.121.250:5002/slogan")
    return (firstname.text + " : " + slogan.text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)

#in this service I collect data from service2&3
#and then communicate this string/json to service 1
