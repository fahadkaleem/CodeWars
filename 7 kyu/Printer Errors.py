# https://www.codewars.com/kata/56541980fa08ab47a0000040

def printer_error(s):
    count = 0
    for i in s:
        if i not in 'abcdefghijklm':
            count +=1
    return "%i/%i"%(count,len(s))