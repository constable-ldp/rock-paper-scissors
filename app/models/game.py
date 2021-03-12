from app.models.player import Player

players = []

def add_player(player):
    players.append(player)

def compare_input(player1, player2):
    if player1.choice == player2.choice:
        return 
    if player1.choice == 'Rock' and player2.choice == 'Scissors' \
    or player1.choice == 'Paper' and player2.choice == 'Rock' \
    or player1.choice == 'Scissors' and player2.choice == 'Paper':
        return player1
    else:
        return player2
