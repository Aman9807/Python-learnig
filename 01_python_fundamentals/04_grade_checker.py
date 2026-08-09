# Question 4: Grade Calculator with Input Validation
#
# Problem Statement:
# Take a student's marks (0-100) and determine their grade using conditional logic (`if-elif-else`).
# Handle invalid marks outside the range 0-100.
#
# Tasks to complete:
# 1. Take `name` and integer `marks` as input.
# 2. Validate if marks are between 0 and 100 inclusive.
# 3. Assign grades: A (>=90), B (>=75), C (>=40), or Failed (<40).
# 4. Print an error message if invalid marks are entered.
#
# Write your code below this line:

name = input("Enter your name\n")
marks = int(input("Enter your marks\n"))
if(marks<=100 and marks>=0):

    if (marks>=90):
        print("A Grade")
    elif(marks>=75):
      print("B Grade")
    elif(marks>=40):
      print("C Grade")
    else:
      print("Failed")

else:
   print("Enter Correct marks")
   