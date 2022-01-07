

number = int(input("what number would you like to check? "))

def find_reverse(number, reversed_number):
    if number < 10:
        reversed_number = (reversed_number*10) + number
        return reversed_number
    else:
        remainder = number % 10
        reversed_number = (reversed_number*10) + remainder
        return find_reverse(number//10, reversed_number)

othernumber = find_reverse(number, 0)
print(othernumber)
if othernumber == number:
    print(True)
else:
    print(False)