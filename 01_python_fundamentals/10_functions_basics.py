# Functions: reusable blocks of code.


def greet(name):
    print(f"Hello, {name}! Welcome to Python functions.")

def is_even(number):

    if number % 2 == 0:
        return True
    
    else:
        return False
    
greet(input("Enter your name: "))

number = int(input("Enter a number to check if it is even or odd: "))
boolean = is_even(number)

if boolean == True:

    print(f"{number} is even.")
else:

    print(f"{number} is odd.")