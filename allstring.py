
def printAllKLengthRec(set, prefix, n, k):
    if k == 0:
        print(prefix)
        return

    for i in range(n):
        newPRefix = prefix + set[i]
        printAllKLengthRec(set, newPRefix, n, k - 1)

def printAllKLength(set, k):
    n = len(set)
    printAllKLengthRec(set, "", n, k)

if __name__ == "__main__":

    print("test one")
    set1 = ["a", "b", "c"]
    k = 3
    printAllKLength(set1, k)