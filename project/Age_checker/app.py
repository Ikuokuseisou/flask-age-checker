from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

def classify_age(age):
    if age <= 14 :
        return "子供"
    elif age <= 18 :
        return  "少年"
    elif age <= 30 :

        return "青年"
    elif age  <= 60:
        return "中年"
    else :
        return "高齢者"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit",methods = ["POST"])
def submit():
    age = request.form.get("age")
    try:
        age = int(age)
    except ValueError :
       return render_template("index.html", error = "数字を入力してください" )
    
    if age < 0 or age > 120 :
        return render_template("index.html",error = "実年齢を入力してください")

    return redirect(url_for("result",age = age))

@app.route("/result")
def result():
    age = request.args.get("age")
    age = int(age)

    category = classify_age(age)

    return render_template("result.html",age = age,category = category)
 
if __name__ == "__main__":
    app.run(debug=True)