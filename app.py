from flask import Flask, render_template, request, redirect, url_for
from universe.hogwarts.main import run_quiz as hogwarts_quiz, QUESTIONS as hogwarts_questions
from universe.chicago.main import run_quiz as chicago_quiz, QUESTIONS as chicago_questions
from universe.olympus.main import run_quiz as olympus_quiz, QUESTIONS as olympus_questions

app = Flask(__name__)

UNIVERSES = {
    "hogwarts": {
        "questions": hogwarts_questions,
        "quiz_func": hogwarts_quiz
    },
    "chicago": {
        "questions": chicago_questions,
        "quiz_func": chicago_quiz
    },
    "olympus": {
        "questions": olympus_questions,
        "quiz_func": olympus_quiz
    }
}

# CHANGED: Added methods=["GET", "POST"] to handle form submissions on home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # If your index.html has a dropdown or button named 'universe'
        selected_universe = request.form.get("universe")
        if selected_universe in UNIVERSES:
            return redirect(url_for("quiz", universe=selected_universe))
    
    return render_template("index.html")

@app.route("/quiz/<universe>", methods=["GET"])
def quiz(universe):
    if universe not in UNIVERSES:
        return redirect(url_for("home"))
    questions = UNIVERSES[universe]["questions"]
    return render_template("quiz.html", universe=universe, questions=questions)

@app.route("/result/<universe>", methods=["POST"])
def result(universe):
    if universe not in UNIVERSES:
        return redirect(url_for("home"))
    
    # Pass the request.form data to your logic function
    result_val = UNIVERSES[universe]["quiz_func"](request.form)
    return render_template("result.html", universe=universe, result=result_val)

if __name__ == "__main__":
    app.run(debug=True)