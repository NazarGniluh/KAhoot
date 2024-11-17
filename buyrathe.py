from flask import *

from dbMAnager import BDManager

app = Flask("kahoot")

db_name = "kahoot.db"

@app.route("/")
def index():
    db_manager = BDManager("kahoot.db")
    qiuzeerss = db_manager.get_quizzer()
    return render_template("index.html", qiuzeerss=qiuzeerss)

@app.route("/about_information")
def about_information():
    return render_template("about_information.html")

app.run()