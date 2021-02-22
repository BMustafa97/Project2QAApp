from flask import Flask, Response, request
import random
import os
from os import getenv

app = Flask(__name__)
@app.route('/slogan')
def slogans():
    slogan = ["We Give You Wings", "Finger-Lickin' Food", "Eat Fresh and Tasty!", "We're always on your mind", "The Best in Manchester", "Freshly Fried!", "The best you can find!"]
    return Response(random.choice(slogan), mimetype="text")
#in this service I create the second part of restaurant

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)