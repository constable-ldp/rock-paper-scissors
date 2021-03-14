from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player
import random

scores = []
players = Game([])
names = []

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/play/restart', methods=['POST'])
def restart():
    players.reset_game()
    names.clear()
    scores.clear()
    return redirect('/')

@app.route('/play-again/restart', methods=['POST'])
def again_restart():
    players.reset_game()
    if names[0] == 'Computer':
        computer = Player('Computer', random.choice(['rock', 'paper', 'scissors']))
        players.add_player(computer)
    return redirect('/play-again')

@app.route('/play')
def play():
    return render_template('play.html', title='Play', players=players.players, names=names)

@app.route('/play', methods=['POST'])
def set_up_game():
    name = request.form['name']
    choice = request.form['choice']
    names.append(name)
    new_player = Player(name, choice)
    players.add_player(new_player)
    return redirect('/play')

@app.route('/play-computer', methods=['POST'])
def play_computer_set_up():
    computer = Player('Computer', random.choice(['rock', 'paper', 'scissors']))
    players.add_player(computer)
    names.append('Computer')
    return redirect('/play')

@app.route('/play-again')
def play_again():
    return render_template('play-again.html', title='Play again', players=players.players, names=names)

@app.route('/play-again', methods=['POST'])
def same_players_reset():
    name = request.form['name']
    choice = request.form['choice']
    new_player = Player(name, choice)
    players.add_player(new_player)
    return redirect('/play-again')

@app.route('/rock/rock', methods=['POST'])
def rock_draw_result():
    return redirect('/result')

@app.route('/rock/scissors', methods=['POST'])
def rock_scissors_result():
    return redirect('/result')

@app.route('/rock/paper', methods=['POST'])
def rock_paper_result():
    return redirect('/result')

@app.route('/paper/rock', methods=['POST'])
def paper_rock_result():
    return redirect('/result')

@app.route('/paper/scissors', methods=['POST'])
def paper_scissors_result():
    return redirect('/result')

@app.route('/paper/paper', methods=['POST'])
def paper_paper_result():
    return redirect('/result')

@app.route('/scissors/paper', methods=['POST'])
def scissors_paper_result():
    return redirect('/result')

@app.route('/scissors/scissors', methods=['POST'])
def scissors_scissors_result():
    return redirect('/result')

@app.route('/scissors/rock', methods=['POST'])
def scissors_rock_result():
    return redirect('/result')

@app.route('/result')
def result():
    winner = players.compare_input(scores)
    return render_template('result.html', title='result', players=players, winner=winner, scores=scores)
