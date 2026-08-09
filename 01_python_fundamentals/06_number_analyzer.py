# Question 6: Number Range Analyzer (Sums & Counts)
#
# Problem Statement:
# Analyze numbers from 1 up to a given positive integer `num`. Calculate the total sum,
# the sum and count of even numbers, and the sum and count of odd numbers using a loop.
#
# Tasks to complete:
# 1. Take a positive integer `num` from the user.
# 2. Loop from 1 to `num` and calculate:
#    - Sum of all numbers.
#    - Sum and count of even numbers (`i % 2 == 0`).
#    - Sum and count of odd numbers (`i % 2 != 0`).
# 3. Display the calculated sums and counts clearly.
#
# Write your code below this line:

num = int(input("Enter a number to analyze:\n"))
sum =0
sum_even = 0
sum_odd = 0
no_even = 0
no_odd = 0
if(num > 0):
    
    for i in range(1,num+1):
        sum += i 
        if(i%2==0):
            sum_even += i
            no_even += 1
        else:
            sum_odd += i
            no_odd += 1


    print(f"The sum of all numbers from 1 to {num} is {sum}")
    print(f"The sum of all even numbers from 1 to {num} is {sum_even} and the count of even numbers is {no_even}")
    print(f"The sum of all odd numbers from 1 to {num} is {sum_odd} and the count of odd numbers is {no_odd}")
else:
    print("Please enter a positive number to analyze.")