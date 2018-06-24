import random as r

def usingRand(inputInteger):
    if inputInteger >= 0 and inputInteger <6:
       return 'output 1'
    elif inputInteger > 5 and inputInteger < 9:
        return 'output 2'
    else:
        return 'output 3'

randVariable = r.randint(0, 10)
howTFDoYouKeepTrackOfTheseVariableTypes = usingRand(randVariable)
print(howTFDoYouKeepTrackOfTheseVariableTypes)