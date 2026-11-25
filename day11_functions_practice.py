#Ex 1 Welcome function
def welcome(name):
    print("Welcome",name)

welcome("Goku")
welcome("Naruto")
welcome("Saitama")

#Ex 2 Calculator function
def calculate(a,b):
    print(a)
    print(b)
    return a + b
    
result = calculate(10, 20)
print(result)
result = calculate(50, 30)
print(result)

#Ex 3 Conditions inside functions
def check_number(number):
    print(number)
    if number > 0:
        print("Positive")
    elif number == 0:
        print("Zero")
    else:
        print("Negative")
check_number(10)
check_number(-5)
check_number(0)

#Mini Quiz App
def question():
    a = input("What is the capital of Pakistan? ")
    if a.lower() == "islamabad":
        print("Correct!")
    else:
        print("Wrong!")
question()
