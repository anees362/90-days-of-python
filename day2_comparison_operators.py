# ex 1 Predict the output

a = 10
b = 20

print(a > b)
print(a < b)
print(a == 10)
print(b != 20)

#ex 2 Age registration

age = int(input("Whats your age: "))

if age >= 18:
    print("You can register")
else:
    print("You cannot register")

# ex 3 Grading program

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail!")
