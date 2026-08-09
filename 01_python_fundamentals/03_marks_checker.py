# Question 3: Pass/Fail Marks Checker
#
# Problem Statement:
# Check whether a student has passed an exam based on a passing criteria of 40 marks.
# If failed, display how many additional marks were needed to pass.
#
# Tasks to complete:
# 1. Take student `name` and integer `marks` as input.
# 2. If `marks >= 40`, print that the student passed.
# 3. If `marks < 40`, calculate `40 - marks` and print how many more marks were needed.
#
# Write your code below this line:

name = input("Enter your name\n")
marks  = int(input("Enter your marks\n"))
if(marks>=40):
    print(f"{name}, you passed")
else:
    print(f"{name}, you failed. You need {40 - marks} more marks to pass")