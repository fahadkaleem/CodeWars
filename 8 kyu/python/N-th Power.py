# https://www.codewars.com/kata/57d814e4950d8489720008db

def index(array, n):
    if n>len(array):
        return -1
    return array[n]**n