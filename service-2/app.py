from flask import Flask, Response, request
import random
import os
from os import getenv

app = Flask(__name__)

@app.route('/firstname')
def firstname():
    firstnames = ["Koolios", "Shakedown", "Benny's", "Whippy", "Deli", "Urban", "Lil-Italia", "Pa-Pa-Peri"]
    return Response(random.choice(firstnames), mimetype="text")
#in this service give the user half of their new username

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)