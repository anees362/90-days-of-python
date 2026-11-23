#ex 1 Predict the output

a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b)


#ex 2 Student discount

age = (int(input("What's your age: ")))
student_id = input("Do you have a student ID? (yes/no): ")
if age < 18 and student_id == "yes":
    print("Discount available")
else:
    print("No discount")


#ex 3 Login checker

username = input("Whats your username: ")
password = input("Whats your password: ")

if username == "admin" and password == "python123":
    print("Login successful")
else:
    print("Incorrect credentials")
