from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)

print(anagram("listen", "silent"))
