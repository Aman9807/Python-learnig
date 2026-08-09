# Question 5: Multiplication Table Generator
#
# Problem Statement:
# Generate and print the multiplication table for any given number from 1 to 10 using a `for` loop.
#
# Tasks to complete:
# 1. Take a number input from the user.
# 2. Use a `for` loop with `range(1, 11)`.
# 3. Print the multiplication table in the format: `number * i = result`.
#
# Write your code below this line:

table = int(input("Enter the number for which you want to print the multiplication table:\n")) 
for num in range(1, 11):
    print(table,"*",num,"=",table*num)
