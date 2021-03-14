from app.models.player import Player
import random

class Game:
    def __init__(self, players):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def compare_input(self, scores):
        scores.append(0)
        scores.append(0)
        if self.players[0].choice == self.players[1].choice:
            scores[0]+=.5
            scores[1]+=.5
            return 
        if self.players[0].choice == 'rock' and self.players[1].choice == 'scissors' \
        or self.players[0].choice == 'paper' and self.players[1].choice == 'rock' \
        or self.players[0].choice == 'scissors' and self.players[1].choice == 'paper':
            scores[0]+=1
            return self.players[0]
        else:
            scores[1]+=1
            return self.players[1]

    def reset_game(self):
        self.players.clear()
