# https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    ret = ""
    for i in str(num):
        ret += str(int(i)**2)
    return int(ret)