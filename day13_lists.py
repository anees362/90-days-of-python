#Ex 1

games = ["Minecraft","Hollow Knight","Sekiro","Batman Arkham Knight"]
print(games)
print(games[0])
games.append("GTA")
games.remove("Sekiro")
print(len(games))
for game in games:
    print(game)

#Ex 2

student = ["James","Tommy","Elon","Nick","Thomas"]
print(student[1])
student[2] = "Mark"
student.append("Robin")
student.remove("James")
print(len(student))
for i in student:
    print(i)
