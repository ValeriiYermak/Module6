import re

def total_salary(path):
    
    rez = 0
    pers_sal = r'\d+'
    file = open(path, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        found = line.strip().split(",")
        found = float(found[1])
        rez = rez + found
           
    file.close()
    return rez

