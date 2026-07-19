from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    return render_template("sample.html")

app.run(debug=True)
