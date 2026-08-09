num = int(input("Enter a number: "))
while num < 1:
    print("Please enter a positive number.")
    num = int(input("Enter a number: "))

print(f"You entered a positive number: {num}")