# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    # ...
    lst = list(map(int,numbers.split(' ')))
    return "%i %i" % (max(lst),min(lst))