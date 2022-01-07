
#basic program to reverse an int for interview practice

number = int(input("please enter any number:  "))

#pulls last number from group of numbers
#recreate the number starting with last number
#remove last digit from number

reverse = 0 
while (number > 0):
    remainder = number % 10
    print(f"reminder: {remainder}")
    reverse = (reverse * 10) + remainder
    print(f"reverse: {reverse}")
    number = number // 10 
    print(f"number: {number}")

print (f"\n Reverse of the entered number is = {reverse}")

