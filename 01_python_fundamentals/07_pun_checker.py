# Question 7: PIN Authentication System (Attempts Counter)
#
# Problem Statement:
# Simulate an ATM PIN verification system allowing a maximum of 3 attempts.
# Exit the loop immediately upon entering the correct PIN or display attempt exhaustion.
#
# Tasks to complete:
# 1. Set a secret 4-digit PIN (e.g., `1234`).
# 2. Use a loop allowing up to 3 attempts.
# 3. Prompt user for PIN input; if correct, print success and `break`.
# 4. If wrong, show remaining attempts left, or print an exhaustion message on the 3rd failed attempt.
#
# Write your code below this line:

pin = 1234

for i in range(3):
    user_pin = int(input("Enter your pin \n"))
    if(user_pin == pin):
        print("Pin is correct")
        break
    else:
        print("Pin is incorrect")
        if(i==2):
            print("You have exhausted all attempts. Please try again later.")
        else:
            print(f"You have {2-i} attempts left.")
