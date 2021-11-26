from flask.templating import render_template
from app import app
from models.player import Player
from models.game import Game

@app.route("/")
def index():
    return "Hello"

@app.route("/<player_1_choice>/<player_2_choice>")
def compare(player_1_choice, player_2_choice):
    player_1 = Player("Player 1",player_1_choice)
    player_2 = Player("Player 2",player_2_choice)
    game = Game()
    winner = game.compare_choices(player_1,player_2)
    return render_template("index.html", title="Game", player_1=player_1, player_2=player_2, winner=winner )
