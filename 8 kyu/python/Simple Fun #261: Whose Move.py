# https://www.codewars.com/kata/59126992f9f87fd31600009b

def whoseMove(lastPlayer, win):
    players = {"white": "black", "black": "white"}
    if win:
        return lastPlayer
    return players[lastPlayer]
