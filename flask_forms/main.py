from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        with open("data.txt","w") as f:
            f.write(f"The name is :{request.form['name']} - with email {request.form['email']} - and message: {request.form['message']}\n")
            return render_template("thanks.html")
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)   