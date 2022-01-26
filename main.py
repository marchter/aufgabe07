from flask import Flask, render_template, session
from model import Question, read_questions, set_questions, get_rand_question, shuffle_answers

app = Flask(__name__)
set_questions()
shuffle_answers()

level = 0


@app.route('/')
def start():
    return render_template("index.html")


@app.route("/questions")
def allQuestionsPage():
    return render_template("questions.html", questions=read_questions())


@app.route("/game")
@app.route("/game/<int:answer>")
def game(answer=-1):
    # TODO: question weitergeben und in die 4 buttons ausgeben
    question = get_rand_question(level)
    return render_template("game_index.html", question=question.get_question(), answers=question.get_answers())


if __name__ == '__main__':
    app.run()
