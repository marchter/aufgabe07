from flask import Flask, render_template, session
from model import read_questions, set_questions, get_rand_question, shuffle_answers

app = Flask(__name__)
set_questions()
shuffle_answers()
app.secret_key = '5#y2L”F4Q8z\n\ xec ]/'
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

    if(answer == -1):
        session['level'] = 0
    elif(session['current_question'] == answer):
        level+1
        print("Richtig")
    else:
        print("Wrong!")
        answer = -1
        return render_template("lost.html")

    question = get_rand_question(level)
    session['current_question'] = question.get_index()
    session['current_level'] = question.get_level()


    return render_template("game_index.html", question=question.get_question(), answers=question.get_answers())


if __name__ == '__main__':
    app.run()