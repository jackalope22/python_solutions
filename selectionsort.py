
from random import randint

def create_array(size=10, max=50):
    return [randint(0,max) for _ in range(size)]

def selection_sort(a):
    sortedLength = 0 
    while sortedLength < len(a):
        min_index = None
        for i,element in enumerate(a[sortedLength:]):
            if min_index == None or element < a[min_index]:
                min_index = i + sortedLength
        a[sortedLength], a[min_index] = a[min_index], a [sortedLength]
        sortedLength += 1
    return a

a = create_array()
print(f" Unsorted {a}")
print(f" Sorted: {selection_sort(a)}")
