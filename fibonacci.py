nterms = int(input("please enter a positive integer: "))

n1, n2 = 0, 1
count = 0 

if nterms <= 0:
    print("please enter positive integer")
elif nterms == 1:
    print(f"Fibonacci sequence upto {nterms}:")
    print(n1)

else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1