from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "John":59,
        "Saurabh":71,
        "Mark":74,
        "Jeff":85,
        "Alexa":95,
        "Lily":100
    }
    return render_template("index.html",marks= marks)


app.run(debug=True)