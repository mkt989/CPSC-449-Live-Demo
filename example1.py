# This file contains an example for a GET request.
from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World!!", 200

if __name__=='__main__':
    app.run()
