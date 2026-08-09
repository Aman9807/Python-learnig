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
