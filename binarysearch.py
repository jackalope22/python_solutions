from math import ceil

def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        mid = ceil(int(mid))
        print("mid"+str(mid))
        guess = list[mid]
        print(guess)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
my_list = [1,2,5,6,7,8,9,10,11,13,14,18,19,20,21,22,24,28,29,30,31,32,33,34,35,36,37]
print(binary_search(my_list, 5))
