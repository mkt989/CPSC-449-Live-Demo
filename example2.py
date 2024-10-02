# This file contains an example for a POST request.

from flask import Flask,request,jsonify
app = Flask(__name__)
app.debug = True

@app.route("/user", methods=["POST"])
def user():
    content = request.json
    return  jsonify(content), 200

if __name__=='__main__':
    app.run()
