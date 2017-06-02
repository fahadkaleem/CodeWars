# https://www.codewars.com/kata/5672a98bdbdd995fad00000f

def rps(p1, p2):
    com = {"paper":"rock", "scissors":"paper", "rock":"scissors"}
    if p1==p2:
        return "Draw!"
    elif(com[p1]==p2):
        return "Player 1 won!"
    else:
        return "Player 2 won!"