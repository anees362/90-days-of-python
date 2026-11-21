
# Ex 1: Predict the output

for i in range(1, 6):
    print(i * 2)

# Ex 2: Number counter

for i in range(0, 10):
    print(i + 1)
print("Finished!")

# Ex 3: Even numbers

for i in range(1, 11):
    print(i * 2)

# Ex 4: Countdown

count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Ex 5: Number guessing game

import random
b = random.randint(1, 10)

while True:
    number = int(input("Try guessing my number 1-10: "))

    if number < b:
        print("Try higher number")
    elif number > b:
        print("Try lower number")
    elif number == b:
        print("That's correct!")
        break
