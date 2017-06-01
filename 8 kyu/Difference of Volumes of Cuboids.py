# https://www.codewars.com/kata/58cb43f4256836ed95000f97

def find_difference(a, b):
    avol = 1
    bvol = 1
    for i in a:
        avol = avol*i
    for i in b:
        bvol = bvol*i
    return abs(avol-bvol)