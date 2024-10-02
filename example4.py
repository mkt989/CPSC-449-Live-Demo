# This file combines all the examples.

from flask import Flask,request,jsonify

app = Flask(__name__)
app.debug = True

global name 
name = "Akanksh"

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World!!", 200

@app.route("/user", methods=["POST"])
def user():
    content = request.json
    return  jsonify(content), 200

@app.route("/user", methods=["GET","PUT"])
def userput():
    global name
    if request.method == "GET":
        return  name , 200
    content = request.json
    name = content["name"]
    return  name, 200

if __name__=='__main__':
    app.run()
