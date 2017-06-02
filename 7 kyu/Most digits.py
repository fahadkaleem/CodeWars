# https://www.codewars.com/kata/58daa7617332e59593000006

def find_longest(arr):
    current = ""
    for i in arr:
        if len(current) < len(str(i)):
            current = str(i)
    return int(current)