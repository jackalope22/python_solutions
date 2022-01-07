from textwrap import indent
from icecream import ic

def solveforx(stringvalue):
    solve = {"+":"-", "-":"+", "*":"/", "/":"*"}

    newstring = stringvalue.split()
    if "x" in newstring:
        posx = newstring.index("x")
    else:
        for i in range(0, len(newstring)):
            if "x" in newstring[i]:
                posx = i
            else:
                pass
    ic(newstring)
    ic(posx)
    if posx == 0:
        solvestring = eval(newstring[4] + solve[newstring[1]] + newstring[2])
    elif posx == 2:
        solvestring = eval(newstring[4] + solve[newstring[1]] + newstring[0])
    else:
        solvestring = eval(newstring[0] + newstring[1] + newstring[2])

    print(solvestring)

solveforx("x + 4 = 10")
solveforx("x - 2 = 8")
solveforx("3 + x = 9")
solveforx("2 + 4 = x")
solveforx("1x0 / 10 = 10")
solveforx("10 * 5 = 5x")