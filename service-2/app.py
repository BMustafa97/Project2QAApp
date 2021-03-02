from flask import Flask, Response, request
import random
import os
from os import getenv

app = Flask(__name__)

@app.route('/firstname')
def firstname():
    firstnames = ["Koolios", "Shakedown", "Benny's", "Whippy - V2", "Deli-V2", "Urban-V2", "Lil-Italia", "Pa-Pa-Peri-V2", "Taco-licious-V2", "Cheesey-Drip", "Pops Diner-V2", "Double-Trouble-V2", "Nashville", "Side-Street-V2"]
    return Response(random.choice(firstnames), mimetype="text")
#in this service give the user half of their new username
@app.route('/firstnametest')
def firstnametest():
    firstnames = ["Koolios"]
    return Response(random.choice(firstnames), mimetype="text")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)