from app.models.player import Player

player1 = Player('John', 'Rock')
player2 = Player('Mary', 'Scissors')

def compare_input(player1, player2):
    if player1.choice == player2.choice:
        return 'Draw'
    if player1.choice == 'Rock' and player2.choice == 'Scissors' \
    or player1.choice == 'Paper' and player2.choice == 'Rock' \
    or player1.choice == 'Scissors' and player2.choice == 'Paper':
        return f'{player1.name} wins!'
    else:
        return f'{player2.name} wins!'