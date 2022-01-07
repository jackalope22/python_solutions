from collections import Counter
from icecream import ic

listone = ["a", "b", "b", "b", "a", "b"]
stringval = {}

for count, value in enumerate(listone):
    stringval[count] = value

for key, value in stringval.items():
    ic(key, value)

results = Counter(stringval.values())
print(results)

def countbetween():
    start = False
    lettercount = 0

    for key, value in stringval.items():
        if value == "a" and start == True:
            return lettercount
        elif value == "a" and start == False:
            start = True
        elif value == "b":
            lettercount +=1
            ic(value, lettercount)
         
ic(countbetween())

