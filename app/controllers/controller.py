from flask import render_template, request, redirect
from app import app
from app.models.game import players, add_player, compare_input
from app.models.player import Player

@app.route('/play')
def index():
    return render_template('index.html', title='Home', players=players)

@app.route('/play', methods=['POST'])
def set_up_game():
    name = request.form['name']
    choice = request.form['choice']
    new_player = Player(name, choice)
    add_player(new_player)
    return redirect('/play')

@app.route('/rock/rock')
def rock_draw():
    winner = compare_input(players[0],players[1])
    return render_template('result.html', title='rock_rock', players=players, winner=winner)

@app.route('/rock/rock', methods=['POST'])
def rock_draw_result():
    return redirect('/rock/rock')

@app.route('/rock/scissors')
def rock_scissors():
    winner = compare_input(players[0],players[1])
    return render_template('result.html', title='rock_scissors', players=players, winner=winner)

@app.route('/rock/scissors', methods=['POST'])
def rock_scissors_result():
    return redirect('/rock/scissors')

@app.route('/rock/paper')
def rock_paper():
    winner = compare_input(players[0],players[1])
    return render_template('result.html', title='rock_paper', players=players, winner=winner)

@app.route('/rock/paper', methods=['POST'])
def rock_paper_result():
    return redirect('/rock/paper')

@app.route('/paper/rock')
def paper_rock():
    winner = compare_input(players[0],players[1])
    return render_template('result.html', title='paper_rock', players=players, winner=winner)

@app.route('/paper/rock', methods=['POST'])
def paper_rock_result():
    return redirect('/paper/rock')

@app.route('/paper/scissors')
def paper_scissors():
    winner = compare_input(players[0],players[1])
    return render_template('result.html', title='paper_scissors', players=players, winner=winner)

@app.route('/paper/scissors', methods=['POST'])
def paper_scissors_result():
    return redirect('/paper/scissors')

@app.route('/paper/paper')
def paper_paper():
    winner = compare_input(players[0],players[1])
    return render_template('result.html', title='paper_paper', players=players, winner=winner)

@app.route('/paper/paper', methods=['POST'])
def paper_paper_result():
    return redirect('/paper/paper')

@app.route('/scissors/paper',)
def scissors_paper():
    winner = compare_input(players[0],players[1])
    return render_template('result.html', title='scissors_paper', players=players, winner=winner)

@app.route('/scissors/paper', methods=['POST'])
def scissors_paper_result():
    return redirect('/scissors/paper')

@app.route('/scissors/scissors')
def scissors_scissors():
    winner = compare_input(players[0],players[1])
    return render_template('result.html', title='scissors_scissors', players=players, winner=winner)

@app.route('/scissors/scissors', methods=['POST'])
def scissors_scissors_result():
    return redirect('/scissors/scissors')

@app.route('/scissors/rock')
def scissors_rock():
    winner = compare_input(players[0],players[1])
    return render_template('result.html', title='scissors_rock', players=players, winner=winner)

@app.route('/scissors/rock', methods=['POST'])
def scissors_rock_result():
    return redirect('scissors/rock')
