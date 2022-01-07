
def chunk(list, size):
    return [list[i:i+size] for i in range(0, len(list), size)]

numbers = [1248, 5478, 658, 4444]
print(chunk(numbers, 2))