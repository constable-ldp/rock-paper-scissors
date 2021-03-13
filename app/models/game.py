from app.models.player import Player

class Game:
    def __init__(self, players):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def compare_input(self):
        if self.players[0].choice == self.players[1].choice:
            return 
        if self.players[0].choice == 'Rock' and self.players[1].choice == 'Scissors' \
        or self.players[0].choice == 'Paper' and self.players[1].choice == 'Rock' \
        or self.players[0].choice == 'Scissors' and self.players[1].choice == 'Paper':
            return self.players[0]
        else:
            return self.players[1]

    def reset_game(self):
        self.players.clear()

    def reset_choice(self):
        print(self.players[0].choice)