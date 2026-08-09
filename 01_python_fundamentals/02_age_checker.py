name = input("Enter your name\n")
age = int(input("Enter your age\n"))
if (age>= 18):
    print(f"{name} a, you are eligible to vote")

else:
    print(f"{name}, you will eligile to in {18-age} years")

