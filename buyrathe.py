from flask import *

from dbMAnager import BDManager

app = Flask("kahoot")

db_name = "kahoot.db"
app.secret_key = "27354826"


@app.route("/")
def index():
    db_manager = BDManager("kahoot.db")
    qiuzeerss = db_manager.get_quizzer()
    return render_template("index.html", qiuzeerss=qiuzeerss)

@app.route("/about_information")
def about_information():
    return render_template("about_information.html")


@app.route("/qiuzz/<int:quizz_id>")
def get_question(quizz_id):
    db_manager = BDManager(db_name)
    questions = db_manager.get_questions(quizz_id)
    session["questions"] = questions
    session["true_ans"] = 0
    session["quest_index"] = 0

    return redirect(url_for("show_question", quizz_id=quizz_id))

@app.route("/qiuzz/<int:quizz_id>/question")
def show_question(quizz_id):
    nomer = session["quest_index"]
    q = session["questions"][nomer]
    db_manager = BDManager(db_name)
    options = db_manager.get_options(q[0])

    return str(q) + "<br>" + str(options)




app.run()