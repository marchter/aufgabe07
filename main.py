from flask import Flask, render_template, session
from model import Question
app = Flask(__name__)

@app.route('/')
def start():
   return render_template("index.html")

@app.route("/game")
@app.route("/game/<int:answer>")
def game(answer = -1):
   #TODO: question weitergeben und in die 4 buttons ausgeben
   return render_template("game_index.html")

if __name__ == '__main__':
   app.run()