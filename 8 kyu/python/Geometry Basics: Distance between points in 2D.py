# https://www.codewars.com/kata/58dced7b702b805b200000be

import math
def distance_between_points(a, b):
    return math.sqrt(((a.x-b.x)**2)+((a.y-b.y)**2))