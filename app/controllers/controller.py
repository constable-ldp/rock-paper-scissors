from flask import render_template, request, redirect
from app import app
from app.models.game import players, compare_input
from app.models.player import Player

@app.route('/events')
def index():
    return render_template('index.html', title='Home', players=players)