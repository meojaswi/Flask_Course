from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Ojaswi"
    age = 22
    if "name" in request.args and "age" in request.args:
        name= request.args["name"]
        age= request.args["age"]
    return render_template("index.html",name= name, age= age)

app.run(debug=True)