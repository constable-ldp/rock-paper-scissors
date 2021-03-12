from flask import render_template, request, redirect
from app import app
from app.models.game import players, add_player, compare_input
from app.models.player import Player

@app.route('/play')
def index():
    if len(players) == 2:
        compare_input(players[0], players[1])
    return render_template('index.html', title='Home', players=players)

@app.route('/play', methods=['POST'])
def set_up_game():
    name = request.form['name']
    choice = request.form['choice']
    new_player = Player(name, choice)
    add_player(new_player)
    return redirect('/play')
