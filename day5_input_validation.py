#Ex 1 Safe number input

try:
    number = int((input("Type a number: ")))
    print(number)
except ValueError:
    print("You can only type a number!")

#Ex 2 Age checker
try:

    age = int(input("Whats your age: "))

    if age < 18:
        print("Your a child")
    elif age >= 18:
        print("Your an adult")
except ValueError:
    print("You can only type numbers")

#Ex3 Positive number checker

try:
    number = int(input("Type a number: "))
    if number < 0:
        print("Your number is negative")
    elif number == 0:
        print("Your number is 0")
    elif number > 0:
        print("Your number is positive")
except ValueError:
    print("You can only type whole numbers!")

#Mini project

import random
rdm = random.randint(1,10)
try:
    for i in range(5):
        number = int(input("Guess my number 1-10: "))

        if number < rdm:
            print("Try higher number")
        elif number > rdm:
            print("Try lower number")
        elif number == rdm:
            print("Thats correct!")
            print("My number was", (rdm))
            break
    else:
        print("Woops you ran out of attempts!")
except ValueError:
    print("You can only type whole numbers!")
