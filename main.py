from flask import Flask, render_template

app = Flask("Website")

# The below @ symbol signifies that this line is a decorator and it
# decorates the below function
@app.route("/")
def home():
    return render_template("sample.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact-us/")
def contact():
    return render_template("contact.html")

@app.route("/store/")
def store():
    return render_template("store.html")

app.run(debug=True)
