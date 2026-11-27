#Mini quiz app
def question():
    score = 0
    a = input("Whats the capital of Egypt? ")
    if a.lower() == "cairo":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
    b = input("Whats the capital of Canada? ")
    if b.lower() == "ottawa":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
    c = input("Whats the capital of Pakistan? ")
    if c.lower() == "islamabad":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
    print("Your score:", score,"/ 3")
question()
