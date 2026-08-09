# Question 2: Voting Eligibility Checker
#
# Problem Statement:
# Take user's name and age as input and check if they are eligible to vote (age 18 or above).
# If not eligible, calculate and display how many years are remaining.
#
# Tasks to complete:
# 1. Take `name` and `age` input from the user.
# 2. Check if `age >= 18`. If true, print that the user is eligible to vote.
# 3. Otherwise, calculate `18 - age` and display the remaining years needed to become eligible.
#
# Write your code below this line:

name = input("Enter your name\n")
age = int(input("Enter your age\n"))
if (age>= 18):
    print(f"{name} a, you are eligible to vote")

else:
    print(f"{name}, you will eligile to in {18-age} years")

