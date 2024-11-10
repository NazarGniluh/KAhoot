from flask import *


app = Flask("kahoot")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about_information")
def about_information():
    return render_template("about_information.html")

app.run()