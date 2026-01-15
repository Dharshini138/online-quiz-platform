from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_questions():
    conn = sqlite3.connect("quiz.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions")
    data = cur.fetchall()
    conn.close()
    return data

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=get_questions())

@app.route("/submit", methods=["POST"])
def submit():
    questions = get_questions()
    score = 0
    results = []

    for q in questions:
        qid = str(q[0])
        selected = request.form.get(f"q{qid}")
        correct = q[6]

        if selected == correct:
            score += 1

        results.append({
            "question": q[1],
            "options": q[2:6],
            "correct": correct,
            "selected": selected
        })

    return render_template(
        "result.html",
        score=score,
        total=len(questions),
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)
