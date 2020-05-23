def computegrade(score):
    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score >= 0.6:
            return 'D'
        else:  
            return 'F'
    else:
        return 'Bad score'

entsc = input('Enter score: ')

try:
    sc = float(entsc)
except ValueError:
    print('Bad score')
    quit()
grade = computegrade(sc)
print (grade)
