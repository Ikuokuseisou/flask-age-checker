from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit",methods = ["POST"])
def submit():
    age = request.form.get("age")
    try:
        age = int(age)
    except ValueError :
       return "数字を入力してください"
    
    if age < 0 or age > 120 :
        return "実年齢を入力してください"

    return redirect(url_for("result",age = age))

@app.route("/result")
def result():
    age = request.args.get("age")
    age = int(age)

    return render_template("result.html",age = age)
 
if __name__ == "__main__":
    app.run(debug=True)