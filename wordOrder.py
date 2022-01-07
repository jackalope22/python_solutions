import sys
new_list = [4, 'bcdef', 'abcdefg', 'bcde', 'bcdef', 'hij', 'hij', 'jklm', 'jklm', 'bcdef', 'abc', 'bcd']

lessRepeats = dict()
total_count = []

for elem in new_list[1:]:
    if elem in lessRepeats:
        lessRepeats[elem] += 1
    else:
        lessRepeats[elem] = 1

for key, value in lessRepeats.items():
    total_count.append(value)

print(len(total_count))
print(*total_count)

