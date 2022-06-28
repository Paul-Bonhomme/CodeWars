from random import randint


def random_rps(player1, player2):
    num = randint(1, 3)
    if num == 1:
        return "Player 1 won!"
    elif num == 2:
        return "Player 2 won!"
    else:
        return "Draw!"


def rps(player1, player2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[player1] == player2:
        return "Player 1 won!"
    elif beats[player2] == player1:
        return "Player 2 wom!"
    else:
        return "Draw!"






