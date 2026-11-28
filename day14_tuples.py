# Ex 1
games = ("Minecraft", "Hollow Knight", "Sekiro", "Batman Arkham Knight")
print(games)
print(games[0])
print(games[3])
print(len(games))

# Ex 2
characters = ("Goku", "Naruto", "Goku", "Luffy", "Goku", "Saitama")
print(characters.count("Goku"))
print(characters.index("Luffy"))
print(characters.index("Saitama"))

# Ex 3
numbers = (10, 20, 30, 40, 50, 60, 70)
print(numbers[:3])
print(numbers[2:5])
print(numbers[-3:])

# Ex 4
player = ("Goku", 25, "Dragon Ball")
name, age, anime = player
print(name)
print(age)
print(anime)
print(name, "is", age, "years old and belongs to", anime)

# Ex 5
scores = (85, 90, 75, 100, 95)
for score in scores:
    print(score)
    print("Passed")
print(sum(scores))

# Ex 6
marks = (20, 10, 80, 50, 90)
for mark in marks:
    print(mark)

print(max(marks))
print(min(marks))
print(sum(marks))
print(len(marks))

average = sum(marks) / len(marks)
print(average)

# Ex 7 - Mini Student Results
marks = (64, 82, 50, 90, 40)

for mark in marks:
    print(mark)

print(max(marks))
print(min(marks))
print(sum(marks))

average = sum(marks) / len(marks)
print(average)

if average >= 80:
    print("Excellent")
else:
    print("Keep Practising")
