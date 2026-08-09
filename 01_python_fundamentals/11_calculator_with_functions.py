# A program to demonstrate the use of functions in Python by making simple calculator.

def add(a , b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

num = float(input("Enter first number: \n"))
operator = input("Enter operator (+, -, *, /):\n ")
num2 = float(input("Enter second number: \n"))

if operator == "+":
    print(f"{num} + {num2} = {add(num , num2)}")

elif operator == "-":
    print(f"{num} - {num2} = {subtract(num , num2)}")

elif operator == "*":
    print(f"{num} * {num2} = {multiply(num , num2)}")

elif operator == "/":
    print(f"{num} / {num2} = {divide(num , num2)}")

else:
    print("Invalid operator. Please use +, -, *, or /.")

