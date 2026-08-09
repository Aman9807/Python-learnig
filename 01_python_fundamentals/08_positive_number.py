# Question 8: Positive Number Input Validator (`while` loop)
#
# Problem Statement:
# Keep asking the user to enter a number until they enter a positive number (>= 1) using a `while` loop.
#
# Tasks to complete:
# 1. Prompt user for a number.
# 2. Use a `while` loop to re-prompt whenever `num < 1`.
# 3. Once a positive number is provided, exit loop and confirm the entered number.
#
# Write your code below this line:

num = int(input("Enter a number: "))
while num < 1:
    print("Please enter a positive number.")
    num = int(input("Enter a number: "))

print(f"You entered a positive number: {num}")