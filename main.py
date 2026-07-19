from flask import Flask, render_template

app = Flask(__name__)

# The below @ symbol signifies that this line is a decorator and it
# decorates the below function
@app.route("/")
def home():
    return render_template("weather.html")

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    temp = 23
    return {"date":date,
            "temprature":temp,
            "station":station}

@app.route("/contact-us/")
def contact():
    return render_template("contact.html")

@app.route("/store/")
def store():
    return render_template("store.html")

if __name__ == "__main__":
    app.run(debug=True)