# https://www.codewars.com/kata/568018a64f35f0c613000054

class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives < 1:
            raise Error('Omae wa mo shindeiru')
        elif self.number == n:
            return True
        self.lives -= 1
        return False
