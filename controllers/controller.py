from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game

@app.route("/")
def index():
    return "Hello"

@app.route("/<player_1_choice>/<player_2_choice>")
def compare_url(player_1_choice, player_2_choice):
    player_1 = Player("Player 1",player_1_choice)
    player_2 = Player("Player 2",player_2_choice)
    game = Game()
    winner = game.compare_choices(player_1,player_2)
    return render_template("index.html", title="Game", player_1=player_1, player_2=player_2, winner=winner )

@app.route("/welcome")
def welcome():
    return render_template("welcome.html", title="Welcome")

@app.route("/play")
def play():
    return render_template("play.html", title="play")

@app.route("/result", methods=["POST"])
def result():
    player_choice = request.form["player_1_choice"]
    player_choice = player_choice.lower()
    print(player_choice)
    player_1= Player("Player 1",player_choice)
    game = Game()
    computer_choice = game.random_computer_choice()
    print(computer_choice)
    player_2 = Player("Computer",computer_choice)
    winner = game.compare_choices(player_1,player_2)
    return render_template("index.html", title="Game", player_1=player_1, player_2=player_2, winner=winner )

