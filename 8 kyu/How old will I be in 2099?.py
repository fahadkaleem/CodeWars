# https://www.codewars.com/kata/5761a717780f8950ce001473

def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    if current_year == year_of_birth:
        return "You were born this very year!"
    elif current_year > year_of_birth:
        return "You are {} year{} old.".format(diff,'s' if diff>1 else '')
    else:
        return "You will be born in {} year{}.".format(diff, 's' if diff>1 else '')