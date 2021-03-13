from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player
import random

players = Game([])
names = []

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/play/restart', methods=['POST'])
def restart():
    players.reset_game()
    names.clear()
    return redirect('/')

@app.route('/play-again/restart', methods=['POST'])
def again_restart():
    players.reset_game()
    return redirect('/play-again')

@app.route('/play')
def play():
    return render_template('play.html', title='Play', players=players.players, names=names)

@app.route('/play', methods=['POST'])
def set_up_game():
    name = request.form['name']
    choice = request.form['choice']
    names.append(name)
    print(names)
    new_player = Player(name, choice)
    players.add_player(new_player)
    return redirect('/play')

@app.route('/play-computer')
def play_computer():
    return render_template('play.html', title='Play', players=players.players)

@app.route('/play-computer', methods=['POST'])
def play_computer_set_up():
    computer = Player('Computer', random.choice(['rock', 'paper', 'scissors']))
    players.add_player(computer)
    return redirect('/play-computer')

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


@app.route('/rock/rock')
def rock_draw():
    winner = players.compare_input()
    return render_template('result.html', title='rock_rock', players=players, winner=winner)

@app.route('/rock/rock', methods=['POST'])
def rock_draw_result():
    return redirect('/rock/rock')

@app.route('/rock/scissors')
def rock_scissors():
    winner = players.compare_input()
    return render_template('result.html', title='rock_scissors', players=players, winner=winner)

@app.route('/rock/scissors', methods=['POST'])
def rock_scissors_result():
    return redirect('/rock/scissors')

@app.route('/rock/paper')
def rock_paper():
    winner = players.compare_input()
    return render_template('result.html', title='rock_paper', players=players, winner=winner)

@app.route('/rock/paper', methods=['POST'])
def rock_paper_result():
    return redirect('/rock/paper')

@app.route('/paper/rock')
def paper_rock():
    winner = players.compare_input()
    return render_template('result.html', title='paper_rock', players=players, winner=winner)

@app.route('/paper/rock', methods=['POST'])
def paper_rock_result():
    return redirect('/paper/rock')

@app.route('/paper/scissors')
def paper_scissors():
    winner = players.compare_input()
    return render_template('result.html', title='paper_scissors', players=players, winner=winner)

@app.route('/paper/scissors', methods=['POST'])
def paper_scissors_result():
    return redirect('/paper/scissors')

@app.route('/paper/paper')
def paper_paper():
    winner = players.compare_input()
    return render_template('result.html', title='paper_paper', players=players, winner=winner)

@app.route('/paper/paper', methods=['POST'])
def paper_paper_result():
    return redirect('/paper/paper')

@app.route('/scissors/paper',)
def scissors_paper():
    winner = players.compare_input()
    return render_template('result.html', title='scissors_paper', players=players, winner=winner)

@app.route('/scissors/paper', methods=['POST'])
def scissors_paper_result():
    return redirect('/scissors/paper')

@app.route('/scissors/scissors')
def scissors_scissors():
    winner = players.compare_input()
    return render_template('result.html', title='scissors_scissors', players=players, winner=winner)

@app.route('/scissors/scissors', methods=['POST'])
def scissors_scissors_result():
    return redirect('/scissors/scissors')

@app.route('/scissors/rock')
def scissors_rock():
    winner = players.compare_input()
    return render_template('result.html', title='scissors_rock', players=players, winner=winner)

@app.route('/scissors/rock', methods=['POST'])
def scissors_rock_result():
    return redirect('/scissors/rock')
