import sys
from itertools import groupby

#for items in sys.stdin:
    #numbers = items
numbers = "1222311"

groups = []
for k, g in groupby(numbers):
    groups.append(f"({len(list(g))}, {k})")
    
print(*groups)