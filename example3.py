# This file contains an example for a PUT and a GET request.

from flask import Flask,request,jsonify
app = Flask(__name__)
app.debug = True

global name 
name = "Akanksh"

@app.route("/user", methods=["GET","PUT"])
def user():
    global name
    if request.method == "GET":
        return  jsonify({"name":name}) , 200
    content = request.json
    name = content["name"]
    return  jsonify({"name":name}), 200

if __name__=='__main__':
    app.run()
